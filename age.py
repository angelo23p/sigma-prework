from datetime import datetime

today = datetime.today()
birth_date_text = input('Enter your birth date (DD/MM/YYYY): ')

birth_date = datetime.strptime(birth_date_text, '%d/%m/%Y')

age = today.year - birth_date.year
if (today.month, today.day) < (birth_date.month, birth_date.day):
    age = age - 1
print(age)