import re

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def normalize_phone(phone_number) -> list:
    """This function is taking a phone number as a string and normalizing it"""
    phone_number = re.sub(r'\D', '', phone_number)  # remove all non-digit characters

    if len(phone_number) == 12:                    # if the number is in international format rerurn it
        return f"+{phone_number}"
    
    elif len(phone_number) == 10:                  # if the number is in national format add the country code
        return f"+38{phone_number}"
    
    elif len(phone_number) == 11:                  # if the number is in national format with 0 at the beginning add the country code
        return f"+3{phone_number}"
    
    elif len(phone_number) == 9:                    # if the number is in national format without the country code add it
        return f"+380{phone_number}"    
                
    else:
        return f"Invalid phone number: {phone_number}"    # if the number is not in any of the above formats return an error message

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)