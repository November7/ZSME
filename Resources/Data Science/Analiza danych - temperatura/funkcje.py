import os

def GetFileFromCurDir(name):
    path = os.path.dirname(__file__)
    return f"{path}\\{name}"


def LatLong(inp):
    last = inp[-1].upper()
    try:
        val = float(inp[:-1])
    except:
        val = 0
    if last == "S" or last == "W":
        return -val
    else:
        return val
    

def F2C(tmp):
    return 5 * (tmp - 32) / 9

# def C2F(tmp):
#     return 9 * tmp / 5 + 32


def AvgLoc(dane):
    return dane.fillna(dane.mean())