def solution(edges, n):
    """ given a multistage graph, edges, find the min path to reach the end of the graph , 0 -> n """
    """ starting from n, find the cost to reach the vertex of each vertex's adj_list """
    cost = [float("infinity")] * (len(edges) + 1)
    """ cost to reach the last node is 0 """
    cost[-1] = 0
    for i in range(len(cost)-2, 0, -1):
        for v, w in edges[i]:
            """ change the cost[i] to be min(edge + cost[v]) """
            cost[i] = min(cost[i], w + cost[v])

    return cost[1]


def solution_adj_list(edges, n):
    """" create an adj_list first """
    """ edges are directed in format [src, dst, w] """
    adj_list = {}
    for src, dst, w in edges:
        if src not in adj_list:
            adj_list[src] = []
        adj_list[src].append((dst, w))

    cost = [float("infinity")] * (len(adj_list) + 1)
    cost[-1] = 0
    for i in range(len(adj_list)-2, 0, -1):
        for v, w in adj_list[i]:
            cost[i] = min(cost[i], w + cost[v])

    return cost[1]

edges = {
    1: [(2, 2), (3, 1), (4, 3)],
    2: [(5, 2), (6, 3)],
    3: [(5, 6), (6, 7)],
    4: [(6, 8), (7, 9)],
    5: [(8, 6)],
    6: [(8, 4)],
    7: [(8, 5)],
    8: [(8, 0)]
}
n = 8

print(solution(edges, n))

edges = [[1, 2, 2], [1, 3, 1], [1, 4, 3], [2, 5, 2], [2, 6, 3], [3, 5, 6], [3, 6, 7], [4, 6, 8], [4, 7, 9], [5, 8, 6], [6, 8, 4], [7, 8, 5], [8, 8, 0]]
n = 8
print(solution_adj_list(edges, n))