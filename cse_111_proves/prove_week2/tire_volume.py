"""
finding the volume of a tire given the width, 
aspect ratio and diameter of the wheel
"""
import math
from datetime import datetime


current_date_and_time = datetime.now()

width = float(input('Enter the width of the tire in mm (ex 205): ')) 

aspect_ratio = float(input('Enter the aspect ratio of the tire (ex 60): '))

diameter = float(input('Enter the diameter of the wheel in inches (ex 15): '))

middle_part = width * aspect_ratio + 2540 * diameter
volume = (math.pi * width ** 2 * aspect_ratio * middle_part) / 10_000_000_000



with open("volume.txt", "at") as volume_file:

    print(f"{current_date_and_time:%Y-%m-%d}, {int(width)}, {int(aspect_ratio)}, {int(diameter)}, {round(volume, 2)}", file=volume_file)
   

print(f'The approximate volume is{volume: .2f} liters')

print('')


buying = input('Would you like to buy tires with these dimesions (yes/no)? ').lower()

if buying == 'yes':
    phone_number = input('Please enter your phone number: ')
    print('Thank you!')

    with open("volume.txt", "at") as volume_file:
        print(f'{phone_number}', file = volume_file)

else:
    print('Have a nice day!')

