from supabase import create_client, Client
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the credentials from environment variables
SUPABASE_URL = os.environ.get('SUPABASE_URL')
SUPABASE_KEY = os.environ.get('SUPABASE_KEY')
def flush_news_table(supabase: Client):
    """
    Deletes all records from the 'news' table in the Supabase database.
    """
    try:
        # Delete all rows in the 'news' table
        response = supabase.table("news").delete().neq('id', 0).execute()
        
        # Check if the response has an 'error' attribute
        if hasattr(response, 'error') and response.error is not None:
            print(f"Error flushing 'news' table: {response.error}")
        else:
            print("All rows deleted from 'news' table.")
    except Exception as e:
        print(f"An error occurred while flushing the 'news' table: {e}")

def flush_database():
    """
    Connects to the Supabase database and flushes the 'news' table.
    """
    # Initialize the Supabase client
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
    
    # Flush the 'news' table
    flush_news_table(supabase)

if __name__ == "__main__":
    flush_database()