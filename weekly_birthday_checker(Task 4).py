import datetime

users = [                                            #if today is 10th March 2024, here are couple of test cases
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "More than week before", "birthday": "1990.03.01"},
    {"name": "Week before", "birthday": "1990.03.03"},
    {"name": "Several days before", "birthday": "1990.03.08"},
    {"name": "Today(Sunday)", "birthday": "1990.03.10"},
    {"name": "Tomorrow", "birthday": "1990.03.11"},
    {"name": "Several days after", "birthday": "1990.03.12"},
    {"name": "6 days after(Saturday)", "birthday": "1990.03.16"},
    {"name": "7 days after(Sunday)", "birthday": "1990.03.17"},
    {"name": "More than week after", "birthday": "1990.03.20"}
]

def get_upcoming_birthdays(users):
    """Function to get upcoming birthdays within 7 days from given list of dictionaries
    and return a list of dictionaries with name and congratulation date
    Congratulation date is set to the next working day if birthday is on Saturday or Sunday
    """
    upcoming_birthdays = []   #return list
    for user in users:
        bday_user = {}       #dictionary for each iteration
        birthday = datetime.datetime.strptime(user["birthday"], "%Y.%m.%d").date()   #convert string to date
        
        today = datetime.date.today()                                   #get today's date
        
        if birthday.replace(year=today.year) < today:          #check if birthday has already passed
            bday_this_year = birthday.replace(year=today.year + 1)      #if yes, set next year's birthday
        else:
            bday_this_year = birthday.replace(year=today.year)          #if no, set this year's birthday
        
        #check if birthday is 29 February and this year is not a leap year
        if birthday.month == 2 and birthday.day == 29 and not (today.year % 4 == 0 and (today.year % 100 != 0 or today.year % 400 == 0)):
            bday_this_year = bday_this_year.replace(day=28)     #set birthday to 28th February
        
        if bday_this_year - today <= datetime.timedelta(days=7):        #check if birthday is within 7 days
            
            if bday_this_year.weekday() == 5:             #check if birthday is on Saturday
                congratulation_date = bday_this_year + datetime.timedelta(days=2)
            
            elif bday_this_year.weekday() == 6:          #check if birthday is on Sunday
                congratulation_date = bday_this_year + datetime.timedelta(days=1)
            
            else:                                    #if birthday is on any other day
                congratulation_date = bday_this_year
            
            
            bday_user["name"] = user["name"]          #add name and birthday to dictionary
            bday_user["congratulation_date"] = congratulation_date.strftime("%Y.%m.%d")
            upcoming_birthdays.append(bday_user)      #append dictionary to list
    return upcoming_birthdays

print(get_upcoming_birthdays(users))
