"""
Variables
"""

cost = 10
tax_percentages = .25
tax = cost * tax_percentages
price = cost + tax

print(price)  # ——> print(10 + (10 * .25))

"""
Strings
"""

username = "ahmad.ali1"
first_name = "Ahmad"
last_name = "Ali"

print(f"{first_name} {last_name}")

first_name = "Muhammad"
print(f"{first_name} {last_name}")

"""
Lists are collections of data
"""


people_list = ["Ahmad", "Muhammad", "Ali"]
# print(people_list)
# print(len(people_list))
# print(people_list[1])
# people_list[1] = "Hafiz"
# print(people_list)
# print(people_list[1])



print(people_list[0:2]) # start with  0 Ahmad and end on 2 Ali but not include Ali



my_list = [80, 96, 72, 100, 8]
print(my_list)

my_list.append(1000)
print(my_list) # [80, 96, 72, 100, 8, 1000]
my_list.insert(2, 1000)
print(my_list) # [80, 96, 100, 72, 100, 8, 1000]

my_list.remove(8)
print(my_list) # [80, 96, 1000, 72, 100, 1000] Remove the first element that is equal to 8

my_list.pop(0)
print(my_list)  # [96, 1000, 72, 100, 1000] Remove the index of the 0 from the list


my_list.sort()
print(my_list)


