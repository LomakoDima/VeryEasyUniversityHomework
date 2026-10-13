n = int(input("Enter n: "))

for number in range(2, n + 1):
    is_prime = True

    for i in range(2, number):
        if i * i > number:
            break

        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(number)
