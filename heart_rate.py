
"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.
"""

age = int(input('Please enter your age: '))

#calculating the maximum heart rate for the entered age
range = 220 - age

#calculating how fast the heart beat is at 65% of the maximum heart rate 
lower_hr = range * 0.65

#calculating how fast the heart beat is at 85% of the maximum heart rate 
upper_hr = range * 0.85

print('When you exercise to strengthen your heart, you should')
print(f'keep your heart rate between{lower_hr: .0f} and{upper_hr: .0f} beats per minute.')
