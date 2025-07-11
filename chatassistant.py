from db import *
import pandas as pd # type: ignore
import streamlit as st # type: ignore
import requests
import json
import os
from datetime import datetime, date
import re


# Database schema information for the LLM
DATABASE_SCHEMA = """
You have access to a PostgreSQL database with the following tables and schema:

1. **income** table:
   - source (VARCHAR): Income source name (e.g., 'paycheck', 'dividends')
   - source_date (DATE): When the income was received
   - amount (DECIMAL): Income amount in USD
   - category (VARCHAR): Income category (e.g., 'earned_income', 'passive_income')
   - ONLY use the columns mentioned in the schema.

2. **expense** table:
   - source (VARCHAR): Expense source name (e.g., 'rent', 'groceries')
   - source_date (DATE): When the expense occurred
   - amount (DECIMAL): Expense amount in USD
   - category (VARCHAR): Expense category (e.g., 'needs', 'wants', 'taxes', 'investments')
   - ONLY use the columns mentioned in the schema.

3. **net_worth** table:
   - source (VARCHAR): Account/asset name
   - source_date (DATE): Date of the net worth snapshot
   - amount (DECIMAL): Account/asset value in USD
   - category (VARCHAR): Asset category (e.g., 'checking', 'investments', 'real_estate')
   - ONLY use the columns mentioned in the schema.

4. **vacation** table:
   - iso_code (VARCHAR): Country code
   - start_date (DATE): Trip start date
   - end_date (DATE): Trip end date
   - city (VARCHAR): Destination city
   - latitude (FLOAT): Location latitude
   - longitude (FLOAT): Location longitude
   - amount (DECIMAL): Trip cost in USD
   - ONLY use the columns mentioned in the schema.

5. **account_info** table:
   - source (VARCHAR): Account name (primary key)
   - description (VARCHAR): Account description with URLs. Use the description to answer questions about the account.
   - updated_at (TIMESTAMP): Last update time
   - ALWAYS use tsquery search in the following format and add & between words of the search_phrase: SELECT * FROM account_info WHERE to_tsvector('english', (source || ' ' || description)::text) @@ to_tsquery('english', 'search_phrase');
   - ONLY use the columns mentioned in the schema.

Current date: {current_date}
"""


def call_ollama(prompt, model="gemma3n"):
    """Call local Ollama API."""
    try:
        # Use environment variable for Ollama host, fallback to localhost
        ollama_host = os.getenv('OLLAMA_HOST', 'localhost')
        ollama_url = f"http://{ollama_host}:11434/api/generate"
        
        response = requests.post(
            ollama_url,
            json={
                "model": model,
                "prompt": prompt,
                "stream": True,
                "options": {
                    "temperature": 0.1,  # Low temperature for more consistent responses
                    "num_predict": 1024
                }
            },
            timeout=30000
        )
        
        if response.status_code == 200:
            # Handle streaming response
            full_response = ""
            for line in response.text.strip().split('\n'):
                if line.strip():
                    try:
                        chunk = json.loads(line)
                        if 'response' in chunk:
                            full_response += chunk['response']
                    except json.JSONDecodeError:
                        continue
            return full_response
        else:
            return f"Error: Ollama API returned status {response.status_code}"
            
    except requests.exceptions.ConnectionError:
        ollama_host = os.getenv('OLLAMA_HOST', 'localhost')
        return f"Error: Could not connect to Ollama at {ollama_host}:11434. Please make sure Ollama is running."
    except requests.exceptions.Timeout:
        return "Error: Request to Ollama timed out."
    except Exception as e:
        return f"Error calling Ollama: {str(e)}"


def extract_sql_from_response(response):
    """Extract SQL query from LLM response."""
    # Look for SQL between ```sql and ``` or ```SQL and ```
    sql_pattern = r'```(?:sql|SQL)?\s*(.*?)```'
    matches = re.findall(sql_pattern, response, re.DOTALL | re.IGNORECASE)
    
    if matches:
        # Return the first SQL query found, cleaned up
        sql = matches[0].strip()
        return sql
    
    # If no code blocks, look for SELECT statements
    select_pattern = r'(SELECT\s+.*?)(?:\n\n|\Z)'
    select_matches = re.findall(select_pattern, response, re.DOTALL | re.IGNORECASE)
    
    if select_matches:
        return select_matches[0].strip()
    
    return None


def generate_sql_query(user_question):
    """Generate SQL query using LLM based on user question."""
    
    current_date = datetime.now().strftime("%Y-%m-%d")
    schema_info = DATABASE_SCHEMA.format(current_date=current_date)
    
    prompt = f"""{schema_info}

Instructions:
1. Generate a PostgreSQL query to answer the user's question
2. Use proper SQL syntax with appropriate JOINs, WHERE clauses, and aggregations
3. ALWAYS use the table name mentioned in the schema.
4. Format monetary values appropriately
5. Use EXTRACT() for date operations when needed
6. Limit results to reasonable numbers (e.g., TOP 10) unless asked for everything
7. ONLY return the SQL query, no explanations
8. ALWAYS include URL for account info queries.
9. ALWAYS check your query for correct table and column names.
10. Wrap the SQL query in ```sql code blocks

User Question: {user_question}

SQL Query:"""

    print(prompt)

    # response = call_ollama(prompt).replace("vcation", "vacation").replace("vaction", "vacation")
    response = call_ollama(prompt)
    print(response)
    sql_query = extract_sql_from_response(response)
    print(sql_query)
    
    return sql_query, response


def format_query_results(results, user_question):
    """Format SQL query results into natural language using LLM."""
    
    if not results:
        return "No data found for your query."
    
    # Convert results to a readable format
    if isinstance(results, list) and len(results) > 0:
        if len(results[0]) == 1:
            # Single column results
            data_str = "\n".join([str(row[0]) for row in results[:20]])  # Limit to 20 rows
        else:
            # Multiple column results - format as table
            data_str = ""
            for row in results[:20]:  # Limit to 20 rows
                data_str += " | ".join([str(item) for item in row]) + "\n"
    else:
        data_str = str(results)
    
    prompt = f"""Based on the user's question and the SQL query results below, provide a natural, conversational response that answers their question.

User Question: {user_question}

Query Results:
{data_str}

Instructions:
1. Format monetary amounts with proper currency symbols and commas
2. Make the response conversational and easy to understand
3. If there are multiple results, summarize the key findings AND show results in bullet points
4. If the results are empty, explain that no data was found
5. Do not include the raw SQL or technical details
6. Keep the response focused and relevant to the question

Natural Language Response:"""

    return call_ollama(prompt)


def correct_formatted_response(user_question, formatted_response, sql_query, results):
    """Correct and improve the formatted response using gemma3n."""
    
    # Convert results to a more readable format for the reasoning model
    if isinstance(results, list) and len(results) > 0:
        if len(results[0]) == 1:
            # Single column results
            results_str = "\n".join([str(row[0]) for row in results[:10]])  # Limit to 10 rows
        else:
            # Multiple column results - format as table
            results_str = ""
            for row in results[:10]:  # Limit to 10 rows
                results_str += " | ".join([str(item) for item in row]) + "\n"
    else:
        results_str = str(results)
    
    correction_prompt = f"""You are a financial data analyst reviewing an AI-generated response. Your task is to improve the response for accuracy, clarity, and completeness.

User Question: {user_question}

SQL Query Used:
```sql
{sql_query}
```

Raw Query Results:
{results_str}

AI-Generated Response:
{formatted_response}

Instructions:
1. Check if the response accurately reflects the data
2. Ensure monetary amounts are properly formatted with $ and commas
3. Verify calculations and summaries are correct
4. Improve clarity and readability
5. Add relevant insights or context if helpful
6. If the response is already good, return it unchanged
7. Be conversational and helpful

Provide the corrected/improved response:"""

    corrected_response = call_ollama(correction_prompt, model="gemma3n")
    
    return corrected_response


def query_database_with_llm(user_question):
    """Main function to process user questions using LLM + SQL RAG."""
    
    # Generate SQL query using LLM
    sql_query, llm_response = generate_sql_query(user_question)
    
    if not sql_query:
        return f"I couldn't generate a SQL query for your question. Here's what I tried to understand:\n\n{llm_response}"
    
    try:
        # Execute the corrected SQL query
        results = run_query(sql_query)
        
        # Format results using LLM
        formatted_response = format_query_results(results, user_question)
        
        # Correct the formatted response using gemma3n
        corrected_response = correct_formatted_response(user_question, formatted_response, sql_query, results)
        
        # Add debug info in expander
        debug_info = f"""
**Original Generated SQL Query:**
```sql
{sql_query}
```

**Original Formatted Response:**
{formatted_response}

**Corrected Response (final):**
{corrected_response}

**Raw Results:** {len(results) if results else 0} rows returned
```
{results}
```
"""
        
        return corrected_response, debug_info
        
    except Exception as e:
        error_msg = f"Error executing SQL query: {str(e)}"
        
        # Try to get LLM to explain the error and suggest a fix
        error_prompt = f"""The following SQL query failed with an error. Explain what went wrong and suggest how to fix it:

SQL Query:
{sql_query}

Error:
{str(e)}

Explanation:"""
        
        explanation = call_ollama(error_prompt)
        
        return f"{error_msg}\n\n**Explanation:**\n{explanation}"


def get_help_message():
    """Generate dynamic help message using LLM."""
    
    prompt = f"""Based on the following database schema, generate a helpful message for users explaining what kinds of questions they can ask:

{DATABASE_SCHEMA.format(current_date=datetime.now().strftime("%Y-%m-%d"))}

Create a friendly help message with example questions they can ask. Make it conversational and encouraging.

Help Message:"""
    
    return call_ollama(prompt)


def display_chat_assistant():
    """Display the LLM-powered chat assistant interface."""
    
    st.write("### 🤖 AI Financial Assistant")
    st.write("Ask me anything about your financial data - powered by local Ollama LLM!")
    
    # Check Ollama connection
    col1, col2 = st.columns([3, 1])
    with col2:
        try:
            ollama_host = os.getenv('OLLAMA_HOST', 'localhost')
            test_response = requests.get(f"http://{ollama_host}:11434/api/tags", timeout=10)
            if test_response.status_code == 200:
                st.success("🟢 Ollama Connected")
            else:
                st.error("🔴 Ollama Error")
        except:
            st.error("🔴 Ollama Offline")
    
    # Initialize chat history
    if "llm_chat_messages" not in st.session_state:
        st.session_state.llm_chat_messages = [
            {"role": "assistant", "content": "Hi! I'm your AI financial assistant powered by Ollama. I can analyze your financial data by writing SQL queries and explaining the results in natural language. What would you like to know about your finances?"}
        ]
    
    # Display chat messages
    for message in st.session_state.llm_chat_messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            
            # Show debug info if available
            if "debug" in message:
                with st.expander("🔍 Debug Info (SQL Query & Verification)"):
                    st.markdown(message["debug"])
    
    # Chat input
    if prompt := st.chat_input("Ask about your financial data..."):
        # Add user message to chat history
        st.session_state.llm_chat_messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Generate and display assistant response
        with st.chat_message("assistant"):
            with st.spinner("🧠 Thinking and querying your data..."):
                # Handle special commands
                if prompt.lower() in ['help', 'what can you do', 'commands']:
                    response = get_help_message()
                    debug_info = None
                else:
                    # Use LLM + SQL RAG
                    result = query_database_with_llm(prompt)
                    if isinstance(result, tuple):
                        response, debug_info = result
                    else:
                        response = result
                        debug_info = None
                
            st.markdown(response)
            
            # Show debug info
            if debug_info:
                with st.expander("🔍 Debug Info (SQL Query & Verification)"):
                    st.markdown(debug_info)
            
        # Add assistant response to chat history
        message_data = {"role": "assistant", "content": response}
        if debug_info:
            message_data["debug"] = debug_info
        st.session_state.llm_chat_messages.append(message_data)
    
    # Control buttons
    col1, col2, col3 = st.columns([1, 1, 3])
    
    with col1:
        if st.button("Clear Chat"):
            st.session_state.llm_chat_messages = [
                {"role": "assistant", "content": "Hi! I'm your AI financial assistant powered by Ollama. I can analyze your financial data by writing SQL queries and explaining the results in natural language. What would you like to know about your finances?"}
            ]
            st.rerun()
    
    with col2:
        if st.button("Help"):
            # Add help message to chat
            help_msg = get_help_message()
            st.session_state.llm_chat_messages.append({"role": "assistant", "content": help_msg})
            st.rerun()
    
    # Model info
    st.caption("Powered by Ollama running locally. Make sure Ollama is installed and running with a model like llama3.2") 