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
    phone_number = re.sub(r'[^0-9+]', '', phone_number)  # remove all non-digit characters except +
    
    
    #if number is starting with +380, return it as is
    if phone_number.startswith("+380"):
        return phone_number
    
    #if number is starting with 380, add + to the beginning
    elif phone_number.startswith("380"):
        return f"+{phone_number}"
    
    #if number is starting with 0, add +38 to the beginning
    elif phone_number.startswith("0"):
        return f"+38{phone_number}"
    
    

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
output = f"Нормалізовані номери телефонів для SMS-розсилки: {sanitized_numbers}"
print(output)