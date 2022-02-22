"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.
"""

heart_rate = 220
age = int(input("What is your age? "))

max_heart_rate = heart_rate - age

low = 65 / 100 * max_heart_rate
high = 85 / 100 * max_heart_rate

print (f"When you exercise to strengthen your heart,") 
print (f"you should keep your heart rate between {low:.0f} and {high:.0f} beats per minute.")
