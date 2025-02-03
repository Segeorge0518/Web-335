// Display all users in the collections:
db.users.find();

//Displays a specific user by their email address:
db.users.find({email:'jback@me.com'})

//Displays a specific user by their last name:
db.users.find({lastName:'Mozart'})

//Displays a specific user by their first name:
db.users.find({firstName:'Richard'})

//Displays a specific user by their employee ID:
db.users.find({employeeId: '1010'})