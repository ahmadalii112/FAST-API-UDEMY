"""
Assignment 1
- You have $50
- you buy an item that is $15
- with a tax of 3%
- print how much you have left
"""


money = 50
item_price = 15
tax_rate = .03

price_with_tax = item_price + (item_price * tax_rate)
left_over = money - price_with_tax
print("$" + str(left_over))


"""
Assignment 2

- Ask the user how many days until their birthday

- Using the print()function. Print an approx. number of weeks until their birthday

- 1 week is = to 7 days.
"""


days = int(input("How many days until your birthday? "))
weeks = days // 7
print(f"You have {weeks} weeks until your birthday!")




"""
Assignment 3
- Create a list of 5 animals called zoo

- Delete the animal at the 3rd index.

- Append a new animal at the end of the list

- Delete the animal at the beginning of the list.

- Print all the animals

- Print only the first 3 animals

"""


zoo = ["lion", "tiger", "elephant", "giraffe", "monkey"]
zoo.pop(2)

zoo.append("whale")

zoo.pop(0)
print(zoo)

print(zoo[:3])






"""
Create a function that takes in 3 parameters(firstname, lastname, age) and

returns a dictionary based on those values
"""

def user_details(firstname,lastname,age):
    return {"firstname":firstname,"lastname":lastname,"age":age}


print(user_details("ahmad","ali1",25))