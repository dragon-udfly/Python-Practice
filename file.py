import math 

values = [1, 0, 2, 3, 2]

buffer = 0

for i in values: 
    buffer += i 

print(f"Buffer: {buffer}") 

value_one = 0
value_two = 0

if buffer % 2 == 0:
    value_one = math.ceil(buffer / 2)
    print(f"Ceil Value: {value_one}")

if buffer % 2 == 1:
    value_two = math.floor(buffer / 2)
    print(f"Floor Value: {value_two}")