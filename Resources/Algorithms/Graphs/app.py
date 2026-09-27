class Point:
    def __init__(self,name, x, y):
        self.name = name
        self.x = x
        self.y = y
    def __str__(self):
        return f"{self.name}=({self.x},{self.y})"
    
    def __repr__(self):
        return f"{self.name}=({self.x},{self.y})"
    @classmethod
    def from_string(cls, strPoint):        
        strPoint = strPoint.replace(" ","")
        strPoint = strPoint.replace("(","")
        strPoint = strPoint.replace(")","")
        parsed = strPoint.split("=")
        if len(parsed) != 2:
            return None
        name = parsed[0]
        
        coord = parsed[1].split(",")
        try:
            x = float(coord[0])
            y = float(coord[1])
        except:
            x = 0
            y = 0

        return cls(name, x, y)


A = Point("A",1,2)
B = Point("B",-1,2)
C = Point("C",1,-2)


D = Point.from_string("D=(123,321)")

points = [A,B,C,D]
connections = [(A,B),(A,C)]
print(points)
print(connections)

