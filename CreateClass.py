class Item: 
    def __init__(self, name, price, quantity):
        self.name= name
        self.price= price 
        self.quantity= quantity

    def calculate_price(self):
        return self.price * self.quantity

item1= Item("Dragon", 1000, 3)
print(f"Name: {item1.name} \nPrice: {item1.price} \nQuantity: {item1.quantity}")
print(f"Total: {item1.calculate_price()}")
