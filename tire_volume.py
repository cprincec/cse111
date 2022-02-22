#import math module.
import math

print ()

#request for width, aspect ratio and diameter from user.
width = float(input("Enter the width of the tire: "))
aspect_ratio = float(input("Enter the aspect ratio of the tire: "))
diameter = float(input("Enter the diameter of the tire: "))

#calculate the volume.
volume = math.pi * width ** 2 * aspect_ratio * (width * aspect_ratio + (2540 * diameter)) / 10000000000

#round the answer to 2 decimal places.
volume = round(volume, 2)

print ()

#print the answer.
print (f"The volume of the tire is {volume} litres.")