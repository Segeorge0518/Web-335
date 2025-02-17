/*
Title: "George_Hands_On_6-1_Aggregate_Queries.js"
Author: Sara George
Date: 2/15/2025
Description: Solutions for Hands-On 6.1: Aggregate Queries
*/

// a.) Display all students
db.students.find();

// b.) Add a new student. Ensure the fields in the new document match the existing fields in the collection:
student = {firstName:'Hairy', lastName:'Potter', studentId:'s1019', houseId:'h1007'};
db.students.insertOne(student);
// Next, prove the new student was added successfully:
db.students.findOne({studentId: 's1019'});

// C.) Update one of the properties from the student you added in step b:
db.students.updateOne({studentId: 's1019'},{$set:{firstName: 'Harry'}});
// Next, prove the property was updated successfully:
db.students.findOne({studentId: 's1019'});

// D.) Delete the student you created in step b:
db.students.deleteOne({firstName: 'Harry'});
// Next, prove the student was removed successfully:
db.students.findOne({studentId: 's1019'});

// E.) Display all students by house:
db.houses.aggregate([{$lookup: {from:"students", localField:"houseId", foreignField:"houseId", as:"student_docs"}}]);

// F.)Display all students in house Gryffindor. The order should be::
db.houses.aggregate([{$match: {'houseId': 'h1007'}},{$lookup: {from:"students", localField:"houseId", foreignField:"houseId", as:"student_docs"}}]);

// G.) Display all students in the house with an Eagle mascot:
db.houses.aggregate([{$match: {'mascot': 'eagle'}},{$lookup: {from:"students", localField:"houseId", foreignField:"houseId", as:"student_docs"}}]);