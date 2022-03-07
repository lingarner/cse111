import random

def main():
    numbers = [16.2, 75.1, 52.3]

    print(numbers)

    append_random_numbers(numbers)
    print(numbers)

    append_random_numbers(numbers, 3)
    print(numbers)


def append_random_numbers(numbers, quantity=1):
    for _ in range(quantity):
        random_number = random.uniform(0, 100)
        random_number_round = round(random_number, 1)
        numbers.append(random_number_round)
        
    
main()