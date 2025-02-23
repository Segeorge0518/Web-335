"""
Name: Sara George
Date: 2/14/2025
Filename: George_usersp2.py
Description: Submission for Exercise 6.3 - Python with MongoDB
"""

from pymongo import MongoClient

client = MongoClient("mongodb+srv://web335_user:s3cret@bellevueuniversity.t9q5e.mongodb.net/?retryWrites=true&w=majority&appName=BellevueUniversity")
db = client['web335DB']
collection = db['users']

import datetime

# Create a new user document and added it to the users collection
gaga = {
  "firstName": "Lady",
  "lastName": "Gaga",
  "employeeId": "0202",
  "email": "LdyGG@me.com",
  "dateCreated": datetime.datetime.now(datetime.timezone.utc)
}

# Insert the document into the users collection
gaga_user_id = db.users.insert_one(gaga).inserted_id

print(db.users.find_one({"employeeId": "0202"}))



# Create an update query to change the user's email address
db.users.update_one(
 {"employeeId": "0202"},
 {
   "$set": {
     "email": "ladygaga@me.com"
   }
 }
)

# Prove the update worked by searching the collection for the user by employeeId
print(db.users.find_one({"employeeId": "0202"}))

#Build a query to remove a user document
result = db.users.delete_one({
  "employeeId": "0202"
})
print(result)
print(db.users.find_one({"employeeId": "0202"}))
