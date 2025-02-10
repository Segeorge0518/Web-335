""" 
    Title: George_lemonadeStandSchedule.py
    Author: Sara George
    Date: 02/08/2025
    Description: Hands-on 3.1: Conditionals, Lists, and Loops Assignment
"""


# List of tasks
tasks = ["buy ingredients for lemonade", "Make lemonade", "Set up the lemonade stand", "Serve customers", "Manage money"]

# Iterate over the list and print to console
for task in tasks:
    print(task)

# List of days
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# Use a for loop to iterate over the list of days and print the day's task to the console. 
for i, day in enumerate(days):
    if day in ["Sunday"]:
        print("It's Sunday! Take a rest!")
    elif day in ["Monday"]:
        print("It's Monday, todays task is to go buy ingredients for lemonade.")    
    elif day in ["Tuesday"]:
        print("It's Tuesday, todays task is to make lemonade.")
    elif day in ["Wednesday"]:
        print("It's Wednesday, todays task is to set up the lemonade stand.")
    elif day in ["Thursday"]:
        print("It's Thursday, todays task is to serve customers.")
    elif day in ["Friday"]:
        print("It's Friday, todays task is to manage money.")
    elif day in ["Saturday"]:
        print("It's Saturday! Take a rest!")
    else:
        print("End of list!")
