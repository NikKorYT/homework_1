import datetime

def date_input() -> datetime.datetime:
    """
    
    Takes a date input from the user and returns a datetime object.
    Error handling is included to ensure the date is in the correct format.

    """
    date_string = input("Enter a date (yyyy-mm-dd): ")
    
    try:
        date = datetime.datetime.strptime(date_string, "%Y-%m-%d")   # Convert input to datetime object
    except ValueError:
        print("Invalid date format. Please enter a date in the format (yyyy-mm-dd).")  
        return date_input()
    
    return date

def get_days_from_today(date) -> int:
    """
    Takes datetime object and returns the number of days from today.

    If input date is later than today, the function will return a negative integer.
    """
    today = datetime.datetime.now()
    difference = (today - date).days
    return int(difference)

print(get_days_from_today(date_input()))