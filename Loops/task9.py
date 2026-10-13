n = int(input("Enter a number: "))

is_prime = n >= 2

for i in range(2, n):
    if i * i > n:
        break

    if n % i == 0:
        is_prime = False
        break

if is_prime:
    print("Prime")
else:
    print("Not prime")
