from db import *
import pandas as pd # type: ignore
import streamlit as st # type: ignore


def get_account_info_data(search_term=None):
    """
    Get account information from the account_info table.
    
    Args:
        search_term: Optional search term to filter by source or description
    
    Returns:
        pandas DataFrame with account information
    """
    
    # Base query to get all account info
    query = """
        SELECT 
            source,
            description,
            updated_at
        FROM account_info 
        ORDER BY source
    """
    
    results = run_query(query)
    
    if not results:
        return pd.DataFrame()
    
    # Convert to DataFrame
    data = []
    for row in results:
        source, description, updated_at = row
        data.append({
            'Account': source,
            'Description': description if description else '',
            'Updated': updated_at
        })
    
    df = pd.DataFrame(data)
    
    # Apply search filter if specified (case-insensitive, real-time)
    if search_term and search_term.strip():
        search_lower = search_term.lower().strip()
        # Search in both account name and description (case-insensitive)
        mask = (
            df['Account'].str.lower().str.contains(search_lower, case=False, na=False, regex=False) |
            df['Description'].str.lower().str.contains(search_lower, case=False, na=False, regex=False)
        )
        df = df[mask]
    
    return df


def get_account_categories():
    """
    Get account categories by extracting common patterns from account names.
    
    Returns:
        List of account categories
    """
    df = get_account_info_data()
    
    if df.empty:
        return []
    
    # Extract categories based on account patterns
    categories = set()
    for account in df['Account']:
        account_lower = account.lower()
        if any(word in account_lower for word in ['checking', 'savings', 'chase', 'marcus']):
            categories.add('Banking')
        elif any(word in account_lower for word in ['401k', 'ira', 'roth']):
            categories.add('Retirement')
        elif any(word in account_lower for word in ['brokerage', 'etrade']):
            categories.add('Investment')
        elif any(word in account_lower for word in ['car', 'camry']):
            categories.add('Vehicles')
        elif any(word in account_lower for word in ['insurance', 'statefarm', 'bluecross']):
            categories.add('Insurance')
        elif any(word in account_lower for word in ['netflix', 'spotify', 'amazon', 'prime']):
            categories.add('Subscriptions')
        elif any(word in account_lower for word in ['rental', 'hoa']):
            categories.add('Real Estate')
        else:
            categories.add('Other')
    
    return sorted(list(categories))


def display_account_info_table(search_term=None):
    """
    Display account information as a Streamlit table with search functionality.
    
    Args:
        search_term: Optional search term to filter results
    """
    
    # Get the data
    df = get_account_info_data(search_term)
    
    if df.empty:
        st.write("No account information found for the selected search term.")
        return None
    
    # Display the table with custom formatting
    st.write("#### Account Directory")
    
    # Prepare display DataFrame with clickable links
    display_df = df.copy()
    
    # Extract URLs from descriptions and create separate columns
    import re
    url_pattern = r'https?://[^\s)]+[^\s.,)]*'
    
    def extract_url_and_clean_description(desc):
        if not desc:
            return "", ""
        
        urls = re.findall(url_pattern, desc)
        
        if urls:
            # Take the first URL found
            main_url = urls[0]
            # Remove URLs from description to clean it up
            clean_desc = re.sub(url_pattern, '', desc).strip()
            # Clean up extra periods and spaces
            clean_desc = re.sub(r'\s+', ' ', clean_desc).strip(' .')
            return clean_desc, main_url
        else:
            return desc, ""
    
    # Apply the function to create clean descriptions and extract URLs
    descriptions_and_urls = display_df['Description'].apply(extract_url_and_clean_description)
    display_df['Description'] = [item[0] for item in descriptions_and_urls]
    display_df['Website'] = [item[1] for item in descriptions_and_urls]
    
    # Create the table with custom column configuration including clickable links
    st.dataframe(
        display_df[['Account', 'Description', 'Website']],  # Reorder columns
        use_container_width=True,
        hide_index=True,
        column_config={
            "Account": st.column_config.TextColumn(
                "Account Name", 
                width="medium",
                help="Name of the account or service"
            ),
            "Description": st.column_config.TextColumn(
                "Description", 
                width="large",
                help="Details about the account"
            ),
            "Website": st.column_config.LinkColumn(
                "Website",
                width="medium",
                help="Click to visit the website"
            )
        }
    )
    
    # Show search statistics
    if search_term:
        st.caption(f"Showing {len(df)} accounts matching '{search_term}'")
    else:
        st.caption(f"Showing all {len(df)} accounts")


def get_account_stats():
    """
    Get statistics about the accounts.
    
    Returns:
        Dictionary with account statistics
    """
    df = get_account_info_data()
    
    if df.empty:
        return {}
    
    # Categorize accounts
    categories = {
        'Retirement': 0,
        'Investment': 0, 
        'Insurance': 0,
        'Subscriptions': 0,
        'Real Estate': 0,
        'Utilities': 0,
        'Car': 0,
        'Education': 0,
        'Other': 0
    }
    
    for description in df['Description']:
        description_lower = description.lower()
        if any(word in description_lower for word in ['401k', 'ira', 'roth']):
            categories['Retirement'] += 1
        elif any(word in description_lower for word in ['investment', 'brokerage']):
            categories['Investment'] += 1
        elif any(word in description_lower for word in ['insurance', 'statefarm', 'bluecross']):
            categories['Insurance'] += 1
        elif any(word in description_lower for word in ['netflix', 'spotify', 'amazon', 'prime', 'subscriptions']):
            categories['Subscriptions'] += 1
        elif any(word in description_lower for word in ['rental', 'hoa']):
            categories['Real Estate'] += 1
        elif any(word in description_lower for word in ['energy', 'gas', 'trash', 'internet', 'phone']):
            categories['Utilities'] += 1
        elif any(word in description_lower for word in ['car']):
            categories['Car'] += 1
        elif any(word in description_lower for word in ['education', '529']):
            categories['Education'] += 1
        else:
            categories['Other'] += 1
    
    return {
        'total_accounts': len(df),
        'categories': categories,
        'accounts_with_urls': len(df[df['Description'].str.contains('http', na=False)]),
        'last_updated': df['Updated'].max() if not df.empty else None
    }
