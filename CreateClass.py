class Item: 
    def __init__(self, name):
        self.name= name

    def calculate_price(self):
        pass

item1= Item("Dragon")
print(f"Name: {item1.name}")
