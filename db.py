import psycopg2 # type: ignore
from psycopg2 import sql # type: ignore
import os


# Connect to PostgreSQL database
def connect_to_db(dbname=None):
    # Use environment variables if available (Docker), otherwise use defaults (local development)
    host = os.getenv("DB_HOST", "localhost")
    database = dbname or os.getenv("DB_NAME", "personal_finance")
    user = os.getenv("DB_USER", "user")
    password = os.getenv("DB_PASSWORD", "")
    port = os.getenv("DB_PORT", "5432")
    
    try:
        connection = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password,
            port=port
        )
        return connection
    except Exception as error:
        print(f"Error connecting to PostgreSQL database: {error}")
        return None
    

# Execute a query
def run_query(query, params=None):
    connection = connect_to_db()
    if connection is None:
        return
    
    try:
        cursor = connection.cursor()
        if params:
            cursor.execute(query, params)  # For queries with parameters
        else:
            cursor.execute(query)  # For queries without parameters
        
        # Try to fetch results (only works for SELECT queries)
        try:
            result = cursor.fetchall()
        except psycopg2.ProgrammingError:
            # No results to fetch (INSERT, UPDATE, DELETE queries)
            result = None
        
        # Commit changes (if running an INSERT, UPDATE, DELETE query)
        connection.commit()
        
        cursor.close()
        return result
    except Exception as error:
        print(f"Error executing query: {error}")
        return None
    finally:
        connection.close()


def get_available_years():
    """Get distinct years from all tables with date columns, sorted in descending order."""
    query = """
    SELECT DISTINCT year_val
    FROM (
        SELECT EXTRACT(YEAR FROM source_date) AS year_val FROM income
        UNION
        SELECT EXTRACT(YEAR FROM source_date) AS year_val FROM expense  
        UNION
        SELECT EXTRACT(YEAR FROM source_date) AS year_val FROM net_worth
        UNION
        SELECT EXTRACT(YEAR FROM start_date) AS year_val FROM vacation
        UNION  
        SELECT EXTRACT(YEAR FROM end_date) AS year_val FROM vacation
    ) years
    WHERE year_val IS NOT NULL
    ORDER BY year_val DESC
    """
    
    results = run_query(query)
    if results:
        # Convert to list of strings for selectbox compatibility
        return [str(int(year[0])) for year in results]
    else:
        # Fallback to current year if no data
        from datetime import datetime
        current_year = datetime.now().year
        return [str(current_year)]