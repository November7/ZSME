import math

# Program obliczający najlepszą (najkrótszą) trasę ze zbioru punktów

#funkcja parsująca punkt z postaci string do słownika np. A=(1,2)

def parsePoint(strpoint:str) -> tuple | None:
    strname = strpoint.split('=')[0]
    strpoint = strpoint.split('=')[1]
    coords = eval(strpoint)
    if len(coords) != 2:
        return None
    
    for i in coords:
        if not isinstance(i, float) and not isinstance(i, int):
            return None
        
    return  strname,coords

#funkcja licząca odległość między dwoma punktami
def distance(point1:tuple | None, point2:tuple | None) -> float | None:
    if not isinstance(point1, tuple) or not isinstance(point2, tuple):
        return None
    
    x1, y1 = point1[1]
    x2, y2 = point2[1]
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5


#budowanie grafu
def buildGraph(connections:list) -> dict:
    graph: dict[str, dict[str, float | None]] = {}
    for conn in connections:
        point1, point2 = conn
        if point1[0] not in graph:
            graph[point1[0]] = {}
        if point2[0] not in graph:
            graph[point2[0]] = {}
        graph[point1[0]][point2[0]] = distance(point1, point2)
        graph[point2[0]][point1[0]] = distance(point1, point2)
        
    return graph

#algorytm Dijkstry

def dijkstra(graph, start, end):
    import math

    unvisited = set(graph.keys())
    distances = {}
    for node in unvisited:
        distances[node] = math.inf

    distances[start] = 0
    nodes = {}

    success = False
    while unvisited:
        nearest = None
        for node in unvisited:
            if nearest is None or distances[node] < distances[nearest]:
                nearest = node
        

        if nearest == end:
            success = True
            break

        
        unvisited.remove(nearest)

        for neighbor, distance in graph[nearest].items():
            dst = distances[nearest] + distance
            if dst < distances[neighbor]:  
                distances[neighbor] = dst
                nodes[neighbor] = nearest  

    
    if not success:
        return None

    path = []
    while end in nodes:
        path.append(end)
        end = nodes[end]
    path.append(start)
    path.reverse()

    return path


#przykładowe punkty

A = parsePoint("A=(0,0)")
B = parsePoint("B=(1,1)")
C = parsePoint("C=(-1.9,1)")
D = parsePoint("D=(0,3)")

paths = [
    (A, B),
    (A, C),
    # (B, C),
    # (B, D),
    (C, D)
]

graf = buildGraph(paths)

print(graf)

print(dijkstra(graf, 'A', 'D'))