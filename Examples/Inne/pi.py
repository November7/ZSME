import random
import math
import time

# ASCI GRAPHICS
TOP_LINE    =   '┌────────────────┬──────────────────┬────────────────────────┬─────────────┬───────────┐'
MID_LINE    =   '├────────────────┼──────────────────┼────────────────────────┼─────────────┼───────────┤'
BOTTOM_LINE =   '└────────────────┴──────────────────┴────────────────────────┴─────────────┴───────────┘'
CLEAR_LINE  =   '──────────────────────────────────────────────────────────────────────────────────────'
COLOR_GREEN =   '\033[92m'
COLOR_RED   =   '\033[91m'
RESET       =   '\033[0m'
ANSI_CODES  = {COLOR_GREEN, COLOR_RED, RESET}

def matchedPI(epi: str, pi: str) -> str:
    idx = next((i for i, (e, p) in enumerate(zip(epi, pi)) if e != p), len(epi))
    return f"{COLOR_GREEN}{epi[:idx]}{RESET}{COLOR_RED}{epi[idx:]}{RESET}"

def vlen(text: str) -> int:
    raw = text
    for seq in ANSI_CODES:
        raw = raw.replace(seq, "")
    return len(raw)

def centerCText(text: str, width: int) -> str:
    strlen = vlen(text)
    if strlen >= width:
        return text
    left_pad = (width - strlen) // 2
    right_pad = width - strlen - left_pad
    return ' ' * left_pad + text + ' ' * right_pad

def main():
    inside = 0
    total = 0
    strEPI = ''
    maxTime = 30
    strPI = f"{math.pi:.15f}"

    print('Enter maximum time for estimating π: ', end='')
    try:
        user_input = input().strip()
        if user_input:
            maxTime = max(1, int(user_input))
    except ValueError:
        pass  # ignore invalid input

    t0 = time.time()

    
    width = len(TOP_LINE)

    print(TOP_LINE)
    print(f'| Iterations (k) | Points (x, y)    |  π:  {strPI} | Total error | Time (s)  |')
    print(MID_LINE)

    while True:
        elapsed = time.time() - t0
        if elapsed >= maxTime:
            break

        x, y = random.random(), random.random()
        if x*x + y*y <= 1:
            inside += 1
        total += 1

        ePI = 4 * inside / total
        error = abs(ePI - math.pi)

        strEPI = f'{ePI:.15f}'
        cPI = matchedPI(strEPI, strPI)

        remaining = maxTime - elapsed
        print(f'\r| {total:<14d} | ({x:.4f}, {y:.4f}) | est: {cPI} | {error:<0.9f} | {remaining:^9.2f} |',
              end='', flush=True)

    print()
    print(BOTTOM_LINE)

    final_msg = f"Final estimate of π: {matchedPI(strEPI, strPI)} after {total} iterations"
    print("|" + centerCText(final_msg, width-2) + "|")

    print(BOTTOM_LINE)

if __name__ == '__main__':
    main()