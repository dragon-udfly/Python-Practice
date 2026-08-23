import numpy as np 

class Turtle: 
    """Turtle blueprint"""

    def __init__(self): 
        self.letters = np.array([
            [['A', 'C', 'R'], ['A', 'B', 'W']],
            [['N', 'U', 'T'], ['G', 'Q', 'O']]
        ])
        self.word = ""
    
    def printDimension(self): 
        print(f"Dimension: {self.letters.ndim}")

    def printShape(self): 
        print(f"Shape: {self.letters.shape}")


if __name__ == "__main__": 
    t1 = Turtle() 
    t1.printDimension()
    t1.printShape()
