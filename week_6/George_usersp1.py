"""
Name: Sara George
Date: 2/14/2025
Filename: George_usersp1.py
Description: Submission for Exercise 6.3 - Python with MongoDB
"""

from pymongo import MongoClient

client = MongoClient("mongodb+srv://web335_user:s3cret@cluster0.lujih.mongodb.net/web335DBretryWrites=true&w=majority")
db = client['web335DB']
collection = db['users']

#Display all documents in the user's collection
all_users = collection.find()
for user in all_users:
    print(user)

#Display document where the employeeId is 1011
employee = collection.find_one({'employeeId': '1011'})
print(employee)

# Display document where the lastName is Mozart
mozart_user = collection.find_one({'lastName': 'Mozart'})
print(mozart_user)