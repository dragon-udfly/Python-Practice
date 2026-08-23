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
            [[3, 3, 2, 2, 3, 0], [4, 5, 9, 4, 3, 0]], 
            [[3, 6, 1, 1, 0, 2], [6, 3, 2, 2, 3, 7]], 
            [[3, 5, 2, 4, 2, 5], [8, 7, 1, 3, 3, 0]]
        ])
    
    def makeWord(self): 
        self.word = self.letters[0, 0, 0] + self.letters[1, 0, 0] + self.letters[1, 1, 2]
        return self.word
    
    def printDimension(self): 
        print(f"Dimension: {self.letters.ndim}")

    def printShape(self): 
        print(f"Shape: {self.letters.shape}")

    def sliceNumbers(self):
        print(f"Result1: \n{self.numbers[1:]}")
        print(f"Result2: \n{self.numbers[0:2:2]}") 
        print(f"Result3: \n{self.numbers[0:2][0]}") 
        # slicing & accessing element
        print(f"Result4: \n{self.numbers[0:2][0][0][0]}")


if __name__ == "__main__": 
    t1 = Turtle() 
 
    t1.sliceNumbers()