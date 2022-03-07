import math

"""
Variable scope: depending on where a variable is declared that is 
where it is used.
functions have an independent scope of everything else 
so using the variable radius in the function
and outside the function because they are stored in seperate
places in memory

radius in compute_circle_area is a completely different
varaiable than the one with the user input
"""
def compute_circle_area(radius):
    area = radius ** 2 * math.pi
    return area

def prompt_user_for_radius():
    r = float(input('enter a radius: '))
    return r 

"""
You can also just declare it as a different variable like
user_radius
"""
# radius = float(input('please enter a radius: '))

print(round(compute_circle_area(prompt_user_for_radius()), 2))
# or
print(f'{compute_circle_area(prompt_user_for_radius): .2f}')
