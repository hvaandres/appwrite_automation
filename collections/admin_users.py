import sys
import os
# Add the parent directory to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

from dotenv import load_dotenv
load_dotenv()

from main import client, db_id, collection_admin_users_id
from appwrite.services.databases import Databases
import secrets

db = Databases(client)

# Create a new collection

admin_users = db.create_collection(
    database_id = db_id,
    collection_id = secrets.token_hex(8),
    name = 'admin-users'
)

print(admin_users)