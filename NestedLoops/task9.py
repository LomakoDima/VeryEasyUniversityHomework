numbers = [10, 20, 30, 40, 50]

target = int(input("Enter a number to search: "))

for number in numbers:
    if number == target:
        print("Found")
        break
else:
    print("Not found")
