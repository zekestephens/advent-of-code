#!/usr/bin/env -S uv run --with numpy --script
import numpy as np

a = np.genfromtxt('input', dtype=int, delimiter=1)

# the actual array is a bit bigger than the input
# it is tiled five time right and down and each tile is one bigger (mod 10)
# the tiles are incremented as follows:
# 0 1 2 3 4
# 1 2 3 4 5
# 2 3 4 5 6
# 3 4 5 6 7
# 4 5 6 7 8
def increm(x: int, y: int) -> int:
    # increment the value by y
    # values range from 1 to 9
    # a value higher than 9 should be rolled over to 1
    # 10 -> 1
    # 11 -> 2
    # ...
    return (x + y) % 9 if (x + y) > 9 else x + y

increm = np.vectorize(increm)
a = np.concatenate((np.concatenate((a, increm(a, 1), increm(a, 2), increm(a, 3), increm(a, 4)), axis=1),
                   np.concatenate((increm(a, 1), increm(a, 2), increm(a, 3), increm(a, 4), increm(a, 5)), axis=1),
                   np.concatenate((increm(a, 2), increm(a, 3), increm(a, 4), increm(a, 5), increm(a, 6)), axis=1),
                   np.concatenate((increm(a, 3), increm(a, 4), increm(a, 5), increm(a, 6), increm(a, 7)), axis=1),
                   np.concatenate((increm(a, 4), increm(a, 5), increm(a, 6), increm(a, 7), increm(a, 8)), axis=1)), axis=0)

np.set_printoptions(threshold=np.inf)


def graphify(a: np.ndarray) -> dict:
    graph = {}
    for i in range(len(a)):
        for j in range(len(a[i])):
            graph[(i, j)] = []
            if i > 0:
                graph[(i, j)].append((i - 1, j))
            if j > 0:
                graph[(i, j)].append((i, j - 1))
            if i < len(a) - 1:
                graph[(i, j)].append((i + 1, j))
            if j < len(a[i]) - 1:
                graph[(i, j)].append((i, j + 1))
    return graph


graph = graphify(a)


def dijkstra_path(graph: dict, weights: np.ndarray, start: tuple, end: tuple) -> int:
    """returns the length of the shortest path from start to end"""
    distances = np.full(weights.shape, np.inf, dtype=np.int32)
    distances[start] = 0
    not_visited = set(graph.keys())
    while not_visited:
        # find the vertex with the smallest distance
        if start in not_visited:
            min_vertex = start
        else:
            min_vertex = min(not_visited, key=lambda v: distances[v])
        # remove the vertex from the not_visited set
        not_visited.remove(min_vertex)
        # update the distances of the neighbors
        for neighbor in graph[min_vertex]:
            if distances[neighbor] > distances[min_vertex] + weights[neighbor]:
                distances[neighbor] = distances[min_vertex] + weights[neighbor]
    return distances[end]

# implement the algorithm with a priority queue
def dijkstra_path_pq(graph: dict, weights: np.ndarray, start: tuple, end: tuple) -> int:
    """returns the length of the shortest path from start to end"""
    distances = np.full(weights.shape, np.inf, dtype=np.int32)
    distances[start] = 0
    not_visited = set(graph.keys())
    pq = [(0, start)]
    while not_visited:
        # find the vertex with the smallest distance
        min_dist, min_vertex = min(pq, key=lambda t: t[0])
        pq.remove((min_dist, min_vertex))
        # remove the vertex from the not_visited set
        not_visited.remove(min_vertex)
        # update the distances of the neighbors
        for neighbor in graph[min_vertex]:
            if distances[neighbor] > distances[min_vertex] + weights[neighbor]:
                distances[neighbor] = distances[min_vertex] + weights[neighbor]
                pq.append((distances[neighbor], neighbor))
    return distances[end]

print(dijkstra_path_pq(graph, a, (0, 0), (-1, -1)))
