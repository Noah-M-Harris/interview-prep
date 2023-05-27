def solution(arr):
    """ given an arr of integers, create every possible permutation """
    result = []

    def dfs(i, path, paths):
        """ invalid base case """
        if i >= len(arr):
            paths.append(path[:])
            return 
        
        """ consider the two cases for position i: including int at i and not including it """
        path.append(arr[i])
        dfs(i+1, path, paths)
        path.pop()
        dfs(i+1, path, paths)

    dfs(0, [], result)
    return result


arr = [1, 2, 3]
print(solution(arr))