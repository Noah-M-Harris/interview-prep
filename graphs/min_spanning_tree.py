import heapq
def min_cost_spanning_tree(edges, n):
    """ given a list of edges and an associated weight between those edges """
    """ find the minimum cost spanning tree """
    adj_list = {}
    for i in range(1, n+1):
        adj_list[i] = []

    for src, dst, w in edges:
        adj_list[src].append((dst, w))
        adj_list[dst].append((src, w))
    
    min_heap = []
    for dst, w in adj_list[1]:
        heapq.heappush(min_heap, [w, 1, dst])

    mst = [] # min spanning tree
    seen = set()
    seen.add(1)

    while len(seen) < n: # when seen == n, means we have visited all vertices
        """ take a snapshot, make sure the node we want to go to is not in seen already """
        w, src, dst = heapq.heappop(min_heap)

        if dst in seen:
            continue
            
        """ if we can travel to vertex we want to go to next, append this edge to mst and and vertex to seen """
        """ and for all its' edges, append them, but make sure node we want to travel to not in visit already """
        mst.append([src, dst])
        seen.add(dst)
        for node, w in adj_list[dst]:
            if node not in seen:
                heapq.heappush(min_heap, [w, dst, node])

    return mst