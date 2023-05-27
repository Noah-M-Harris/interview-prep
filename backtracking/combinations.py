def solution(n, k):
    """
    given two nums, n and k,
    return all possible combinations
    of size k choosing from values 
    1 to n
    """

    def dfs(num, path, paths):
        """ valid base case """
        if len(path) == k:
            paths.append(path[:])
            return


        """ invalid base case """
        if num > n:
            return
        
        """ consider the two cases for any num, include and don't include """
        path.append(num)
        dfs(num + 1, path, paths)
        path.pop()

        dfs(num + 1, path, paths)

    paths = []
    dfs(1, [], paths)
    return paths


n, k = 5, 2
print(solution(n, k))
