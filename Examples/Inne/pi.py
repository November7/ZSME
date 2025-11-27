import random
import math
import time

COLOR_GREEN = '\033[92m'
COLOR_RED   = '\033[91m'
RESET       = '\033[0m'
ANSI_CODES  = [COLOR_GREEN, COLOR_RED, RESET]

COL_WIDTH = 22
COL_WIDTHS = [COL_WIDTH] * 5

def matchedPI(epi: str, pi: str) -> str:
    idx = next((i for i, (e, p) in enumerate(zip(epi, pi)) if e != p), len(epi))
    return f'{COLOR_GREEN}{epi[:idx]}{RESET}{COLOR_RED}{epi[idx:]}{RESET}'

def vlen(text: str) -> int:
    for seq in ANSI_CODES:
        text = text.replace(seq, '')
    return len(text)

def alignCText(text: str, width: int, align: str = '^') -> str:
    strlen = vlen(text)
    if strlen >= width:
        return text

    pad = width - strlen

    if align == '<':  
        return text + ' ' * pad
    elif align == '>': 
        return ' ' * pad + text
    else:              
        left_pad = pad // 2
        right_pad = pad - left_pad
        return ' ' * left_pad + text + ' ' * right_pad

def line(left: str, mid: str, right: str) -> str:
    return left + mid.join('─' * w for w in COL_WIDTHS) + right

# def header(cells:list[str], align: str = '^') -> str:
#     return '│' + ''.join(f' {cell:{align}{w-2}} │' for cell, w in zip(cells, COL_WIDTHS))

def header(cells: list[str], align: str = '^') -> str:
    return '│ ' + ' '.join(alignCText(cell, w-2, align) + ' │' for cell, w in zip(cells, COL_WIDTHS))

def main():
    inside = total = 0
    strEPI = ''
    maxTime = 0.1
    strPI = f'{math.pi:.15f}'
    align = '^'

    print('Enter maximum time for estimating π: ', end='')
    try:
        user_input = input().strip()
        if user_input:
            maxTime = max(0.1, float(user_input))
    except ValueError:
        pass

    t0 = time.time()
    width = len(line('┌', '┬', '┐'))

    print(line('┌', '┬', '┐'))
    print(header(['Iterations [k]', 'Points (x, y)', f'π: {strPI}', 'Error', 'Time [s]'], align=align))
    print(line('├', '┼', '┤'))

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

        cols = [
            f' {total:{align}{COL_WIDTH-2}} ',
            f' {(f'({x:.4f}, {y:.4f}) '):{align}{COL_WIDTH-2}} ',
            f' {alignCText(cPI, COL_WIDTH-2, align=align)} ',
            f' {error:{align}{COL_WIDTH-2}.9f} ',
            f' {remaining:{align}{COL_WIDTH-2}.2f} '
        ]
        print(f'\r│{('│'.join(cols))}│', end='', flush=True)

    print()
    print(line('├', '┴', '┤'))

    final_msg = f' Final estimate of π: {matchedPI(strEPI, strPI)} after {total} iterations '
    print('│' + alignCText(final_msg, width-2,align=align) + '│')
    print(line('└', '─', '┘'))

if __name__ == '__main__':
    main()