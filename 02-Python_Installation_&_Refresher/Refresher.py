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




"""
Sets are similar to lists but they are unordered and they don't allow duplicates and use curly brackets {}
"""


my_set = {1, 2, 3, 4, 5, 1, 2}
print(my_set) # {1, 2, 3, 4, 5}
print(len(my_set)) # 5 (5 unique items)


for x in my_set:
    print(x)


# print(my_set[0]) # Error: Sets do not support indexing


my_set.discard(3)
print(my_set) # {1, 2, 4, 5}

my_set.clear()
print(my_set) # set()


my_set.add(6)
print(my_set) # {6}

my_set.update([7, 8, 9])
print(my_set) # {6, 7, 8, 9}




"""
Tuples
"""


my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
print(len(my_tuple))

print(my_tuple[1])

# my_tuple[1] = 100 # Error: Tuples are immutable



""" Boolean and Operators"""



like_coffee = True
like_tea = False

print(like_coffee, like_tea)


print(1 == 2)
print(1 != 2)
print(1 > 2)


# logical Operators
print(True and False)
print(True or False)
print(not True) #( means !  true



""" if ELSe!"""

x = 1

if x == 1:
    print("x is equal to 1")
else:
    print("x is not equal to 1")



"""
Dictionaries are similar to lists but they use curly brackets {} and they are unordered
"""


user_info = {
    "username": "ahmad.ali1",
    "first_name": "Ahmad",
    "last_name": "Ali"
}

print(user_info["username"])
print(user_info.get('username'))

user_info["married"] = True

print(user_info)


for x,y in user_info.items():
    print(x, y)


user_dict = {"username": "ahmad.ali1", "age": 25}
user_dict2 = user_dict

user_dict2.pop("age")
print(user_dict) # {"username": "ahmad.ali1"}

user_dict3 = user_dict.copy() # this will copy the dictionary not the reference
user_dict3.pop("username")
print(user_dict)