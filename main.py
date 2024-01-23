# Started January, 23 2024
# Due January, 29 2024
# Written by Rivar Yoder and Hunter Schoch
# This program takes in the users hourly salary, the hours they work per week,
# the amount of days worked per week, the holidays off per year, and vacation days.
# The program will then give an unadjusted salary estimation where the hourly rate
# is multiplied by the hours worked per day and the average amount of work days per
# year (260). It will then give an adjusted number that subtracts the holidays and
# vacation days.

DASH_LENGTH = 40
# Establishes a 40 character width limit for the dividing lines for aesthetic purposes

print('=' * DASH_LENGTH)
print('SALARY CALCULATOR PROGRAM :)')
print('=' * DASH_LENGTH)

COLUMN_LENGTH = 25
# Forces user entries to be a specific width for aesthetic purposes

salary_hrs = float(input(f"{'Salary per hour':.<{COLUMN_LENGTH}}: "))
# User inputs their hourly rate to be multiplied with an 8-hour work day and total days(260)

daily_hrs = float(input(f"{'Hours per Day':.<{COLUMN_LENGTH}}: "))
# The amount of hours worked per week

days_per_week = float(input(f"{'Days per Week':.<{COLUMN_LENGTH}}: "))
# The amount of days worked per week

holiday_year = float(input(f"{'Holidays per Year':.<{COLUMN_LENGTH}}: "))
# Amount of days the work place is closed in a year

vacation_days = float(input(f"{'Vacation Days per Year':.<{COLUMN_LENGTH}}: "))
# Amount of days the user takes off during the year

print('=' * DASH_LENGTH)
# Calculations
# Calculations
print('=' * DASH_LENGTH)

print('Hope this helps! :)')
