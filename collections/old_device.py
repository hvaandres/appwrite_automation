import sys
import os
# Add the parent directory to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

from dotenv import load_dotenv
load_dotenv()

from main import client, db_id, collection_admin_users_id
from appwrite.client import Client
from appwrite.services.databases import Databases
import secrets

project_id = os.getenv('APPWRITE_PROJECT_ID')
api_key = os.getenv('APPWRITE_API_KEY')
db_id = os.getenv('APPWRITE_DB_ID')

client = Client()
client \
    .set_endpoint('https://cloud.appwrite.io/v1') \
    .set_project(project_id) \
    .set_key(api_key)

db = Databases(client)

# Create a new collection

try:
    # Example: Creating a collection
    old_devices = db.create_collection(
        database_id=db_id,
        collection_id=secrets.token_hex(8),
        name='old-devices'
    )
    print(old_devices)
except Exception as e:
    print(f"Error: {e}")