# Hermetyzacja
# Enkapsulacja

class T:
    def __init__(self):
        self.x = 123
        self._x = 456
        self.__x = 789 #private




ob = T()

print(ob.x)
print(ob._x)
print(ob.__x)