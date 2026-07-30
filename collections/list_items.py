fruits = ["orange", "apple", "banana", "mango", "woodapple"]

print(f"Fruits: \n{fruits}")
print(f"Item: {fruits[2]}")
print(f"Item: {fruits[3]}")

print(f"Length: {len(fruits)}")

if "orange" in fruits:
    print("Orange exists.")

for item in fruits:
    print(item, end = " ")