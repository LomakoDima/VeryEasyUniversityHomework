a = int(input("Enter a: "))
b = int(input("Enter b: "))

a = abs(a)
b = abs(b)

while b != 0:
    a, b = b, a % b

print("GCD:", a)
