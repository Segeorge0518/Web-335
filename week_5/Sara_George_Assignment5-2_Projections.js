/*
Author: Sara George
Date: 2/9/2025
Description: Hands-On 5.1 Mongo DB Document Manipulation and Projections
*/

/*
Part A.)
*/
//Details for the user to be added
user = {firstName: 'Frederic', lastName: 'Chopin', employeeId: 'FC123', email: 'frederic.chopin@me.com', dateCreated: new Date()};

//Publish the user to database
db.users.insertOne(user);

//Finds the new user to ensure they were properly added to the database.
db.users.findOne({firstName: 'Frederic'});


/*
Part B.)
*/
//Updates the email for the already extant entry of Mozart
db.users.updateOne({firstName: "Wolfgang"}, {$set:{email: 'mozart@me.com'}});
//Finds the newly updated entry of Mozart by employeeId
db.users.findOne({employeeId: '1009'});

/*
Part C.)
*/
//Displays all entries in the users collection while only showing the first name, last name, and email
db.users.find({},{_id: 0, firstName: 1, lastName: 1, email: 1});
