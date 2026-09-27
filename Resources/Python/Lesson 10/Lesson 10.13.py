def checkClassMember(obj,member):
    ret = f"{member} is " 
    member = str(member)
    if isinstance(obj, type):
        objType = obj  
        pureObj = objType()
        obj = objType()
    else:
        objType = type(obj)
        pureObj = objType()      
 
    if member in vars(objType):
        if callable(vars(objType)[member]):
            return ret+"a method"
 
    inDir = member in dir(obj)
    inVars = member in vars(obj)
    inPure = member in dir(pureObj)
 
    if inDir and inPure and inVars:
        return ret+"an instance attribute"
    elif inDir and inPure and not(inVars):
        return ret+"a static attribute"
    elif inDir and not(inPure) and inVars:
        return ret+"a dynamic instance attribute"
    else:
        return ret+"is undefined"
 
class T:
    x = 1 # atrybut statyczny
    def __init__(self) -> None:
        self.y = 2 # atrybut instancji
  
ob = T()
setattr(ob, "z", 3)
 
print("Dla klasy T:")
print(checkClassMember(T,"x"))
print(checkClassMember(T,"y"))
print(checkClassMember(T,"z"))
 
print("Dla obiektu klasy T:")
print(checkClassMember(ob,"x"))
print(checkClassMember(ob,"y"))
print(checkClassMember(ob,"z"))
