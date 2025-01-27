"""
Author: Your Name
Date: Current Date
File Name: example.py
Description: This file demonstrates the use of both file header comments and normal
level comments
"""

#Calculate the total costs of making the lemonade
def calculate_cost(lemons_cost, sugar_cost):
    return lemons_cost + sugar_cost 
    
#Calculate the end profits from selling lemonade
def calculate_profit(lemons_cost, sugar_cost, selling_price):
    return selling_price - lemons_cost - sugar_cost

#variables
lemons_cost = 2.5
sugar_cost = 1.5
selling_price = 5

total_cost = calculate_cost(lemons_cost, sugar_cost)
profit = calculate_profit(lemons_cost, sugar_cost, selling_price)

#output the cost and profits to console 
output = f"The total cost of making the lemonade is ${total_cost}, and with a selling price of ${selling_price} there is a total profit of ${profit}."
print(output)