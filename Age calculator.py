import datetime
today = datetime.datetime.now()
current_year = today.year
current_month = today.month
current_day = today.day
year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
day = int(input("Enter the day: "))
birth_date = datetime.datetime(year, month, day)
if birth_date > today:
    print("Year Invalid")
    exit()
age = today - birth_date
years = age.days // 365
remaining_days = age.days % 365
months = remaining_days // 30
days = remaining_days % 30
print(f"You have lived {years} years, {months} months!")
