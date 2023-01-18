from collections import defaultdict
import heapq


def prims(graph, starting_vertex):
    mst = defaultdict(set)
    visited = set([starting_vertex])
    edges = [
        (cost, starting_vertex, to)
        for to, cost in graph[starting_vertex].items()
    ]
    heapq.heapify(edges)

    while edges:
        cost, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst[frm].add(to)
            for to_next, cost in graph[to].items():
                if to_next not in visited:
                    heapq.heappush(edges, (cost, to, to_next))

    return mst

g = {
    'A': {'C': 2},
    'B': {'A': 1},
    'C': {'B': -2},
    'D': {'A': -4, 'C': -1},
    'E': {'D': 1},
    'S': {'A': 10, 'E': 8}
}

print(dict(prims(g, 'S')))