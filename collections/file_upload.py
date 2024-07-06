import secrets
import sys
import os

# Add the parent directory to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

from dotenv import load_dotenv
load_dotenv()

# Now the main module can be imported
from main import client, db_id
from appwrite.services.databases import Databases

db = Databases(client)

# Create a new collection

try:
    # Example: Creating a collection
    file_upload = db.create_collection(
        database_id=db_id,
        collection_id=secrets.token_hex(8),
        name='file_upload'
    )
    print(file_upload)
except Exception as e:
    print(f"Error: {e}")
