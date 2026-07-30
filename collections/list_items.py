fruits = ["orange", "apple", "banana", "mango", "woodapple"]

print(f"Fruits: \n{fruits}")
print(f"Item: {fruits[2]}")
print(f"Item: {fruits[3]}")

print(f"Length: {len(fruits)}")

fruits[4] = "pineapple" # update item
fruits.append("berry") # add item at the end

fruits.remove("banana") # removing item

if "orange" in fruits:
    print("Orange exists.")

for item in fruits:
    print(item, end = " ")