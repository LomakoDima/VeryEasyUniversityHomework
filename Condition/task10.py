day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

if year < 1 or month < 1 or month > 12:
    print("Invalid date")
else:
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        february = 29
    else:
        february = 28

    days_in_month = [
        31, february, 31, 30, 31, 30,
        31, 31, 30, 31, 30, 31
    ]

    if 1 <= day <= days_in_month[month - 1]:
        print("Valid date")
    else:
        print("Invalid date")
