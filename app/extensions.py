import pymongo
from pymongo import MongoClient
import os

# MongoDB Atlas connection URI
# uri = "mongodb+srv://dheerajsharma5869:stI9W2ko9ErVSRZp@webhooksproject.pp1efcm.mongodb.net/webhooksproject?retryWrites=true&w=majority"
# uri = 'mongodb+srv://user:user_pin@dbcluster.frhqp.mongodb.net/?retryWrites=true&w=majority&appName=dbcluster'

uri = os.getenv('MONGODB_URI')
def add_document(data):
    try:
        # Create a MongoClient instance
        with MongoClient(uri) as client:
            # Access the database and collection
            db = client.get_database("webhooksproject")
            collection = db.get_collection("webhook")
            
            # Insert the provided data into the collection
            result = collection.insert_one(data)
            print(f"Document inserted successfully with ID: {result.inserted_id}")
            # return result.inserted_id

    except pymongo.errors.ConnectionFailure as cf_error:
        print(f"Connection to MongoDB failed: {cf_error}")

    except Exception as e:
        print(f"Error occurred: {e}")

