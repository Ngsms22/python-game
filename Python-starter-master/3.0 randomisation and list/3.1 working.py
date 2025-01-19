# import pi
import random
# genaerate random numbers between 1 and 4
random_numbers =random.randint(0, 4)
# print(random_numbers)
# print(pi.PI)
# the random method generate numbers btwn 0 and 0.999999 

# print(random.random)

names = ["matthew", "kelvin", "soler", "jason"]
# print(names)
# adding names to the list of names method-append()
# names.append("Beleh")
# print(names)
# print(names[2])

# how many items are inside of the list
# my_length = len(names)
# print(my_length)
# inserting names in a particular location insert(x,y) x= position or index to insert, y= the item to insert
# another_name = names.insert(1,"Brandon")
# print(names)
# print(another_name)

# popping(removing from a list)

# item_removed = names.pop(1)
# print(names)
# print(item_removed)
# print("removed name from list")
# print(names)
# item_removed2 = names.pop(3)
# print(names)
# name1_removed = names.remove("matthew")
# print(name1_removed)
# kelvin = names.remove("kelvin")
# print(names)


# SLICING a list of numbers

# numbers= [12,23,14,17,19]
# [x,y]-> geting elements starting and including x to but not including 
# [1:3]

# print(numbers[1:3])
# [ :x] printing form 0 to index x and not including x

# print(numbers[ :3])

friends = ["John", "keley", "mike", "tom","peter"]
# print(f"{friends[random_numbers]} pays")
# choice
prson_to_pay= random.choice(friends)
print(f"the person to pay is {prson_to_pay}")
