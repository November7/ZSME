class CExample:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y: return True
        else: return False
 
a = CExample(1, 2)
b = CExample(1, 2)
c = CExample(1, 3)
 
print(a == b) # True
print(a == c) # False
