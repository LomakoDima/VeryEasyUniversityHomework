a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

if a > 0 and b > 0 and c > 0:
    if a + b > c and a + c > b and b + c > a:
        if a == b and b == c:
            print("Equilateral")
        elif a == b or a == c or b == c:
            print("Isosceles")
        else:
            print("Scalene")
    else:
        print("Invalid triangle")
else:
    print("Invalid side lengths")
