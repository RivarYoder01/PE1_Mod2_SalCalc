# Header

DASH_LENGTH = 40
print('=' * DASH_LENGTH)
print('SALARY CALCULATOR PROGRAM :)')
print('=' * DASH_LENGTH)

# Input Code
# Gets Salary per hour
print("What is your hourly rate?")
salary_hrs = float(input())

# Gets total hours per week
print("How many hours do you work in a week?")
# Hunter Should we leave this as a float if they put like 45.5 hours a week?
weekly_hrs = float(input())

# Gets total days worked per week
print("How many Days do you work a week?")
days_per_week = input()

# Gets total holidays off per year
print("How many holidays do you get off every year?")
holiday_year = input()

# Gets total vacation days
print("How many vacation days do you get for the year?")
vacation_days = input()

# Test print code can be removed and replaced when we are ready to make the columns
print(salary_hrs)
print(weekly_hrs)
print(days_per_week)
print(holiday_year)
print(vacation_days)
# Summary Code

COLUMN_LENGTH = 25
print(float(input(f"{'Salary per hour':.<{COLUMN_LENGTH}}: {salary_hrs}")))
print(float(input(f"{'Hours per week':.<{COLUMN_LENGTH}}: {weekly_hrs}")))
print(float(input(f"{'Days worked per week':.<{COLUMN_LENGTH}}: {days_per_week}")))
print(float(input(f"{'Holidays in place':.<{COLUMN_LENGTH}}: {holiday_year}")))
print(float(input(f"{'Vacation days taken':.<{COLUMN_LENGTH}}: {vacation_days}")))