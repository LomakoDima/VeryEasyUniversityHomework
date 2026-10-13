n = int(input("Enter a number: "))

n = abs(n)
count = 0

if n == 0:
    count = 1
else:
    while n > 0:
        n //= 10
        count += 1

print("Digits:", count)
