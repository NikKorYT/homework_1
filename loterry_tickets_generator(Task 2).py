import random


def get_user_input() -> tuple:
    """
    Taking the input from the user, and checking if the input is valid
    """

    min = int(input("Enter the minimum number(>0): "))
    if min < 1:
        print("The minimum number must be greater than 0")
        return input()

    max = int(input("Enter the maximum number(max 1000): "))
    if min < 1:
        print("The minimum number must be greater than 0")
        return input()

    elif max > 1000:
        print("The maximum number must be less than 1000")
        return input()

    quantity = int(
        input(
            f"Enter the quantity of numbers(greater that {min}, but lower than {max}): "
        )
    )
    if quantity < min or quantity > max:
        print(
            f"The quantity of numbers must be greater than {min} and lower than {max}"
        )
        return input()

    return min, max, quantity


def get_numbers_ticket(min, max, quantity) -> list:
    print(f"Generating {quantity} numbers between {min} and {max}")
    numbers = []
    number = 0
    for number in range(quantity):
        new_number = random.randint(min, max)
        while new_number in numbers:
            new_number = random.randint(min, max)
        numbers.append(new_number)
        number += 1
    return sorted(numbers)


print(get_numbers_ticket(*get_user_input()))
