n = int(input("Enter a number: "))

original = n
n = abs(n)
reversed_number = 0

while n > 0:
    digit = n % 10
    reversed_number = reversed_number * 10 + digit
    n //= 10

if original >= 0 and original == reversed_number:
    print("Palindrome")
else:
    print("Not palindrome")
