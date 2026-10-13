year = int(input("Enter year: "))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    leap = True
else:
    leap = False

days = 29 if leap else 28

print("Leap year:", leap)
print("Days in February:", days)
