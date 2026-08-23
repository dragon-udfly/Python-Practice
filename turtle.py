import numpy as np 

class Turtle: 
    """Turtle blueprint"""

    def __init__(self): 
        self.letters = np.array([
            [['A', 'C', 'R'], ['A', 'B', 'W']],
            [['N', 'U', 'T'], ['G', 'Q', 'O']]
        ])
        self.word = ""

        self.numbers = np.array([
            [[3, 3, 2], [2, 3, 0]], 
            [[3, 6, 1], [1, 0, 2]], 
            [[3, 5, 2], [4, 2, 5]]
        ])
    
    def makeWord(self): 
        self.word = self.letters[0, 0, 0] + self.letters[1, 0, 0] + self.letters[1, 1, 2]
        return self.word
    
    def printDimension(self): 
        print(f"Dimension: {self.letters.ndim}")

    def printShape(self): 
        print(f"Shape: {self.letters.shape}")


if __name__ == "__main__": 
    t1 = Turtle() 
    t1.printDimension()
    t1.printShape()

    print(f"Word: {t1.makeWord()}")
