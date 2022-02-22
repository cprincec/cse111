#import math module.
import math

#import datetime class from datetime module.
from datetime import datetime

#print a blank line.
print ()

#request for tire width.
width = float(input("Enter the width of the tire: "))
#request for tire width S.I. unit.
width_unit = input("What is the unit of width? (mm/in): ")
#request for tire aspect ratio.
aspect_ratio = float(input("Enter the aspect ratio of the tire: "))
#request for tire diameter.
diameter = float(input("Enter the diameter of the tire: "))
#request for tire diameter S.I. unit.
diameter_unit = input("What is the unit of diameter? (mm/in): ")

#compute the volume based on S.I. unit provided.
if width_unit == "mm":
    #calculate the volume.
    volume = math.pi * width ** 2 * aspect_ratio * (width * aspect_ratio + (2540 * diameter)) / 10000000000

elif width_unit == "in":
    width = width * 25.4
    #calculate the volume.
    volume = math.pi * width ** 2 * aspect_ratio * (width * aspect_ratio + (2540 * diameter)) / 10000000000

if diameter_unit == "in":
    #calculate the volume.
    volume = math.pi * width ** 2 * aspect_ratio * (width * aspect_ratio + (2540 * diameter)) / 10000000000

elif diameter_unit == "mm":
    width = width / 25.4
    #calculate the volume.
    volume = math.pi * width ** 2 * aspect_ratio * (width * aspect_ratio + (2540 * diameter)) / 10000000000


#round the answer to 2 decimal places.
volume = round(volume, 2)

#print a blank line.
print ()

#print the computed volume.
print (f"The approximate volume of the tire is {volume} litres.")

#print a blank line.
print ()

#get current date and time into the current_datetime variable.
current_datetime = datetime.now()

#open a file called Volumes.txt in reading and append mode.
#save it into a variable called file. 
with open("volumes.txt", "at") as volumes_txt:
  
   #append the current_time, width, aspect ratio, diameter and volume to the volumes_txt file.
   print (f"Current Date: {current_datetime:%y-%m-%d}, Width: {width}, Aspect Ratio: {aspect_ratio}, Diameter: {diameter}, Volume: {volume} liters", file=volumes_txt)