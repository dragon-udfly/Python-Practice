class Item: 
    pay_rate= 0.7
    def __init__(self, name: str, price: float, quantity: int, has_numpad: bool):
        self.name= name
        self.price= price 
        self.quantity= quantity
        self.has_numpad= has_numpad

    def calculate_price(self):
        return Item.pay_rate * self.price * self.quantity

item1= Item("Dragon", 1000, 3, True)
print(f"Name: {item1.name} \nPrice: {item1.price} \nQuantity: {item1.quantity}\nNumpad: {item1.has_numpad}")
print(f"Total: {item1.calculate_price()}")

print(f"Class level attributes: \n{Item.__dict__}")
print(f"Instance level attributes: \n{item1.__dict__}")
