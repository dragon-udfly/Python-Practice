text = "2323233"
text1 = "232 323f"
text2 = " "

# the string contains only numbers
print(f"Sample: {text}\tisDigit: {text.isdigit()}")
print(f"Sample: {text1}\tisDigit: {text1.isdigit()}")
print(f"Sample: {text2}\tisDigit: {text2.isdigit()}")

word = "typewriter"
# string only have alphabetical characters.
print(f"Sample: {word}\tisAlphabetical: {word.isalpha()}")
print(f"Sample: {text}\tisAlphabetical: {text.isalpha()}")

# counting characters or substring 
count = text.count("2")
print(f"Sample: {text}\t Count of 2: {count}")

# replace character of substring
# return updated string
replaced_text = text.replace("2", " ")
print(f"Sample: {text}\tReplaced: {replaced_text}")