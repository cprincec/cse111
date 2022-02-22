import math

#name of the program
print("""\nWelcome to the 'boxes.py' program. 
This program decides how many boxes you need to pack a given number of items.\n""")

#request for the number of items to pack.
nitems = int(input("How many items do you want to pack? "))

#request for number of items per box.
item_per_box = int(input("How many items per box? "))

#compute the number of boxes needed.
nbox = nitems / item_per_box

#round the number of boxes needed to an integer.
nbox = math.ceil(nbox)

print (f"To pack {nitems} items {item_per_box} per box, you will need {nbox} boxes.")