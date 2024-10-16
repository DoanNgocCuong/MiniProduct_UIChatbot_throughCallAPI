import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Load environment variables from .env file
load_dotenv()

# Get the MongoDB URI from the environment variables
uri = os.getenv("MONGO_URI")

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")

    # Write test log to MongoDB
    db = client['test_database']
    collection = db['test_logs']
    test_log = {
        "message": "This is a test log entry"
    }
    result = collection.insert_one(test_log)
    print(f"Test log written with id: {result.inserted_id}")

except Exception as e:
    print(e)