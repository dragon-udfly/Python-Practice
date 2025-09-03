class Calc:
    def __init__(self, num1: float, num2: float):
        # creating assert statements to validate parameters 
        assert num1 >= 0, f"num1 {num1} is not greater than or equal to zero"
        assert num2 >= 0, f"num2 {num2} is not greater than or equal to zero"

        # initializing attributes 
        self.num1= num1 
        self.num2= num2