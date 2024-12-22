import sys
import os
import itertools
import networkx as nx

def BrutForce(m,n,k,bit,bajt):
    ...
    rekonstrukcje = 0
    
    for wariacja in itertools.permutations(range(1, m + 1), n):
        
        isOk = True
        for (x,y) in bit:
            if not((wariacja[x - 1],wariacja[y - 1]) in bajt or (wariacja[y - 1],wariacja[x - 1]) in bajt):
                isOk = False
                break
        
        if isOk:
            for i, w in enumerate(wariacja):
                print(f"{i+1} -> {w}",end=", " )
            print()
            rekonstrukcje += 1

    return f"{rekonstrukcje = }, wynik = {rekonstrukcje % k}"

def Gotowiec(m, n, k, bit, bajt):
    ...
    grBit = nx.Graph(bit)
    grBajt = nx.Graph(bajt)
    rekonstrukcje = nx.algorithms.isomorphism.GraphMatcher(grBajt, grBit)
    lista_rek = list(rekonstrukcje.subgraph_isomorphisms_iter())
    for rek in lista_rek:
        for key,val in rek.items():
            print(f"{key} -> {val}",end=", " )
        print()

    return f"rekonstrukcje = {len(lista_rek)}, wynik = {len(lista_rek) % k}"


def Main():
    ...
    testy = f"{os.path.dirname(__file__)}\\input.txt"
    
    with open(testy, 'r') as file: 
        sys.stdin = file 
        

        for line in sys.stdin:
            line = line.strip()
            if line != "":
                Bitada = []
                Bajtogrod = [] 
                n, m, k = list(map(int,line.split(" ")))
                for _, line in zip(range(n-1),sys.stdin):               
                    x,y = list(map(int,line.split(" ")))
                    Bitada.append((x,y))

                for _, line in zip(range(m-1),sys.stdin):
                    i,j = list(map(int,line.split(" ")))
                    Bajtogrod.append((i,j))
         

                # Sprawdzanie wszystkich wariacji i zliczanie tych, które są możliwe 

                # print(BrutForce(m,n,k,Bitada,Bajtogrod))

                # https://networkx.org/documentation/stable/reference/algorithms/isomorphism.vf2.html
                print(Gotowiec(m,n,k,Bitada,Bajtogrod))
          


if __name__ == "__main__":
    Main()