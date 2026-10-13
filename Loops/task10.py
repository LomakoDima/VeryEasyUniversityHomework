n = int(input("Enter a number: "))

sign = -1 if n < 0 else 1
n = abs(n)
reversed_number = 0

while n > 0:
    digit = n % 10
    reversed_number = reversed_number * 10 + digit
    n //= 10

print("Reversed:", sign * reversed_number)
