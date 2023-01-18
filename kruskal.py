INF = float('inf')
g = [[INF, INF,2, INF, INF, INF],
     [1,INF, INF, INF, INF,INF],
     [INF, -2, INF, INF, INF,INF],
     [-4, INF,-1, INF, INF, INF],
     [INF, INF, INF, 1, INF,INF],
     [10, INF, INF, INF,8,INF]]

V = 6
parent = [i for i in range(V)]

def find(i):
    while parent[i] != i:
        i = parent[i]
    return i

# Does union of i and j. It returns
# false if i and j are already in same
# set.
def union(i, j):
    a = find(i)
    b = find(j)
    parent[a] = b
    
def kruskalMST(cost):
    mincost = 0 # Cost of min MST

    # Initialize sets of disjoint sets
    for i in range(V):
        parent[i] = i

    # Include minimum weight edges one by one
    edge_count = 0
    while edge_count < V - 1:
        mi = INF
        a = -1
        b = -1
        for i in range(V):
            for j in range(V):
                if find(i) != find(j) and cost[i][j] < mi:
                    mi = cost[i][j]
                    a = i
                    b = j
        union(a, b)
        print('Edge {}:({}, {}) cost:{}'.format(edge_count, a, b, mi))
        edge_count += 1
        mincost += mi

    print("Minimum cost= {}".format(mincost))

    
kruskalMST(g)
