import math 

a = float(input("Side A Length: "))
b = float(input("Side B Length: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"Value of C: {round(c, 2)}")