year = int(input('enter a year: '))

# What is in a leap year?
# Year can be evenly divisible by 4
# If the year can be evenlly divisible by 100, it is NOT a leap year, unless
# The year is also evenly divisible by 400, then it is a leap year

# 2000 & 2400 are leap years
# 2300 and 2500 are NOT leap years

# def is_leap(year):
#     if ((year%4==0 and year%100!=0) or (year%400==0)):
#         return true

def is_leap(year):
    leap = False
    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True
    return leap

print(is_leap(year))

