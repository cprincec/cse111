#import the datetime class from the datetime module.
from datetime import datetime

#print the name of the program.
print ("""Welcome to the Discount Calculator Program.""")

#request for a subtotal amount.
subtotal = float(input("Please enter your subtotal amount: "))

#save the current date and time into the current_date variable.
current_date = datetime.now()

#save the current weekday (as an int) into the current_day variable.
current_day = current_date.weekday()

if subtotal >= 50 and (current_day == 1 or current_day == 2):
    discount = 0.1 * subtotal
    new_subtotal = subtotal - discount
    tax = 0.06 * new_subtotal
    total = new_subtotal + tax 
    print (f"Discount amount: {discount:.2f}")
    print (f"Salestax amount: {tax:.2f}")
    print (f"Total: {total:.2f}")

else:
    tax = 0.06 * subtotal
    total = subtotal + tax
    print (f"Salestax amount: {tax:.2f}")
    print (f"Total: {total:.2f}")