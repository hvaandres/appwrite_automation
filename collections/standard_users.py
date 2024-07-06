import sys
import os
# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dotenv import load_dotenv
load_dotenv()

from main import client, db_id
from appwrite.services.databases import Databases
from appwrite.permission import Permission
from appwrite.role import Role
import secrets

db = Databases(client)

# Create a new collection

try:
    standard_users = db.create_collection(
        database_id = db_id,
        collection_id = secrets.token_hex(8),
        name = 'standard-users',
        permissions = [
            Permission.create(Role.users()),
            Permission.read(Role.users()),
            Permission.update(Role.users())
        ]
    )

    print(standard_users)
except Exception as e:
    print(f"Error: {e}")
