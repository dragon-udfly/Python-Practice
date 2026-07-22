text = "This is nothing abd3023 3002"

length = len(text)
print(f"Length of text: {length}\n")

# find first occurance of given sub text
# -1 if not found
occ_space = text.find("xz ")
if occ_space > 0:
    print(f"First Occurance of Space: {occ_space}\n")
else:
    print("Not Found\n")

# find last occurance of given sub text 
# -1 if not found
last_occ = text.rfind(" ")
if last_occ > 0:
    print(f"Last Occurance: {last_occ}\n")
else: 
    print("Not Found.\n")

