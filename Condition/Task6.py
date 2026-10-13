number = int(input("Enter a three-digit number: "))

if 100 <= number <= 999:
    hundreds = number // 100
    tens = (number // 10) % 10
    units = number % 10

    total = hundreds**3 + tens**3 + units**3

    if total == number:
        print("Armstrong number")
    else:
        print("Not an Armstrong number")
else:
    print("Please enter a three-digit number")
