import random
import math

inside = 0
all = 0

mDigits = 0
strPI = f"{math.pi:.15f}"

print('Enter number of matched digits (default: 3): ', end='')
try:
    user_input = input()
    if user_input.strip():
        mDigits = int(user_input)
        if mDigits < 3:
            mDigits = 3
        elif mDigits > 15:
            mDigits = 15
except ValueError:
    ... # ignore invalid input and use default

line = '+--------------+------------------+------------------------+-------------+' 

print(line)
print(f'| K-iterations | Points (x, y)    | PI:  {strPI} | Total error |')
print(line)

while True:
    x = random.random()
    y = random.random()
    if (x - 0.5)**2 + (y - 0.5)**2 < 0.25:
        inside += 1
    all += 1
    ePI = 4 * inside / all
    error = math.fabs(ePI - math.pi)
    
    strEPI = f'{ePI:.15f}'
    cPI = ''        
    strEqual = ''

    for t, e in zip(strPI, strEPI):
        if t == e: strEqual += e                
        else: break


    if all % 100 == 0:
        
        cPI = f'\033[92m{strEqual}\033[0m'  # zielone dla zgodnych cyfr
        cPI += f'\033[91m{strEPI[len(strEqual):]}\033[0m'  # czerwone dla reszty
        print(f"\r| {all//1000:<12d} | ({x:.4f}, {y:.4f}) | est: {cPI} | {error:<0.9f} |", end='', flush=True)
    
    if len(strEqual[2:]) >= mDigits:          
        break

print()
print(line)
msg = f"Final estimate of PI: {strEPI} after {all} iterations"

print(f"| {msg:^{len(line) - 4}} |")

print(line)
