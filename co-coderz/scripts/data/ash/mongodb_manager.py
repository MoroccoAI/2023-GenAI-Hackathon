# mongodb_manager.py

import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")  # Fetch the MongoDB URI from the environment variable
DB_NAME = "awesome_selfhosted"

def connect_to_mongodb():
    try:
        client = MongoClient(MONGO_URI)
        print("Connected to MongoDB successfully!")
        return client
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        return None

def insert_or_update_data(client, category_name, json_content):
    try:
        db = client[DB_NAME]
        collection = db[category_name]

        # Check if the document already exists
        existing_document = collection.find_one({"name": json_content["name"]})
        if existing_document:
            # Update the existing document
            collection.replace_one({"_id": existing_document["_id"]}, json_content)
            print(f"Updated data in MongoDB collection '{category_name}' for file '{json_content['name']}' successfully!")
        else:
            # Insert a new document
            collection.insert_one(json_content)
            print(f"Inserted data into MongoDB collection '{category_name}' for file '{json_content['name']}' successfully!")

    except Exception as e:
        print(f"Error inserting or updating data into MongoDB: {e}")
