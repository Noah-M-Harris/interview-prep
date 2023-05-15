

def create_adjaceny_list(graph):
    """ given a list of pairs, travelling from [src, dst] output an adjacency list """
    """ these pairs are are directed moving from src to dst """
    adj_list = {}
    for src, dst in graph:
        """ create the key for both src and dst then append dst to src val list """
        if src not in adj_list:
            adj_list[src] = []
        if dst not in adj_list:
            adj_list[dst] = []

        adj_list[src].append(dst)

    return adj_list



graph = [[1, 3], [3, 2], [5, 1], [4, 5], [6, 7], [7, 8], [7, 1]]
print(create_adjaceny_list(graph))


def create_adj_list_weights(graph):
    """ given a list of edges, [src, dst, weight], create an adjacency list as well as a weights list """
    """ the nodes are undirected, return the adjacency list as well as the weights list """
    pass
