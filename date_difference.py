from datetime import date
f_date = date(1990, 9, 23)
l_date = date(2021, 9, 23)
delta = l_date - f_date
age = delta / 365
print(delta.days)
print(age)