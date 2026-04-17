import time
import os



def draw(towers, n):
    width = 50
    os.system('cls')

    print("\nAktualny stan:")

    for name, tower in towers.items():
        print(f"{name}:")

        # ile pustych poziomów trzeba dodać na górze
        empty_levels = n - len(tower)

        # najpierw puste poziomy
        for _ in range(empty_levels):
            print()  # pusta linia słupka

        # potem krążki od największego do najmniejszego
        for disk in reversed(tower):
            print(" " * (width//2 - disk) + "=" * (disk * 2 - 1))

        print()

    print("-" * width)
    time.sleep(0.5)


def hanoi(n, left, mid, right, towers):
    if n == 1:
        disk = towers[left].pop()
        towers[right].append(disk)
        draw(towers, len(towers["A"]) + len(towers["B"]) + len(towers["C"]))
        return

    hanoi(n - 1, left, right, mid, towers)

    disk = towers[left].pop()
    towers[right].append(disk)
    
    draw(towers, len(towers["A"]) + len(towers["B"]) + len(towers["C"]))

    hanoi(n - 1, mid, left, right, towers)


if __name__ == '__main__':
    n = 10  # liczba krążków

    towers = {
        "A": list(range(n, 0, -1)),
        "B": [],
        "C": []
    }

    draw(towers, n)
    hanoi(n, "A", "B", "C", towers)
