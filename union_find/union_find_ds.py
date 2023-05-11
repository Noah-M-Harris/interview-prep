"""

Suppose that we are given an array of edges, edges: [1,2], [4,1], [2,4], and we are asked to build a graph and detect a cycle. 
Here, each array in edges is an undirected, connected pair of vertices, i.e. 1 is connected to 2, so on and so forth.

"""
class UnionFindDict:
    def __init__(self, n):
        self.par = {}
        self.rank = {}

        # initalize the par with each node as its own parent
        # initalize rank for each node with 0

        for i in range(1, n + 1):
            self.par[i] = i
            self.rank[i] = 0


    def find(self, node):
        # find the parent of this particular node
        p = self.par[node]

        while p != self.par[p]:
            # while parent != parent, continue traversing upwards
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    def union(self, n1, n2):
        # given two nodes, determine if there exists a cycle
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            # p2's parent becomes p1
            self.par[p2] = p1
        elif self.rank[p2] > self.rank[p1]:
            self.par[p1] = p2
        else:
            # rank is the same, increase either or rank of one
            # define one to be child of other
            self.par[p2] = p1
            self.rank[p1] += 1
        return True

class UnionFind:
    
    
    def __init__(self, n):
        self.rank_arr = [-1] * (n + 1)
        """ each idx refers to itself, eg. idx 2 refers to the node 2 in edges, -1 refers to it being its own parent having rank 1 """

    def find(self, node):
        # for a given node, find the parent node, just look at val stored in idx
        # if val < 0, means it is its own parent of rank abs(val), else it's parent is val go to idx val
        while True:
            if self.rank_arr[node] < 0:
                # we found the parent of node, return it
                return node
            else:
                # go to the val stored at this idx
                node = self.rank_arr[node]

    def union(self, node1, node2):
        # union 2 nodes, if they are in the same set return false, else union these two disjoint sets
        # parent becomes one with the > rank, if they are the same, make either one the parent
        p1, p2 = self.find(node1), self.find(node2)

        if p1 == p2:
            return False
        elif abs(self.rank_arr[p1]) > abs(self.rank_arr[p2]):
            # p1 becomes parent, add the rank of p2 to this node
            self.rank_arr[p1] += self.rank_arr[p2]
            self.rank_arr[p2] = p1
        else:
            self.rank_arr[p2] += self.rank_arr[p1]
            self.rank_arr[p1] = p2
        
        return True


def detect_cycle(edges, n):
    # edges: [1,2], [4,1], [2,4]
    # n = max num in the edges, eg. 4
    union = UnionFind(n)

    for src, dest  in edges:
        if not union.union(src, dest):
            # means we detected a cycle
            return False
    # we have detected no cycles
    return True

def detect_cycle2(edges, n):
    # edges: [1,2], [4,1], [2,4]
    # n = max num in the edges, eg. 4
    union = UnionFindDict(n)

    for src, dest  in edges:
        if not union.union(src, dest):
            # means we detected a cycle
            return False
    # we have detected no cycles
    return True

edges = [[1,2], [4,1], [2,4]]
n = 4
print(detect_cycle(edges, n))
print("2:", detect_cycle2(edges, n))

edges = [[1,2], [4,1]]
n = 4
print(detect_cycle(edges, n))
print("2:", detect_cycle2(edges, n))

edges = [[1,2], [3,1], [2, 4], [5, 7], [6, 8]]
n = 8
print(detect_cycle(edges, n))
print("2:", detect_cycle2(edges, n))