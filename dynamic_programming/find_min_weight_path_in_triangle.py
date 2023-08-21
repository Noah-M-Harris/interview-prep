'''
take as input a triangle of numbers and return the weight of a minimum weight path
'''


def solution(triangle):
    # assuming input is always valid and we always have atleast one level, we want to find
    # triangle[0][0] + min(dfs_call)
    # store in dp (level, i) -> the level we are at and the index @ that level, which stores the val route

    levels = len(triangle)
    dp = {}
    def dfs(level, i):
        if (level, i) in dp:
            return dp[(level, i)]
        
        if level >= levels:
            return 0
        
        # pick min path in next level of dfs(level + 1, i), dfs(level + 1, i + 1)
        dp[(level, i)] = float('inf')
        for n in range(i, min(len(triangle[level]), i + 2)):
            dp[(level, i)] = min(dp[(level, i)], triangle[level][i] + dfs(level + 1, n))
        return dp[(level, i)]
    return dfs(0, 0)



triangle = [[2], [4, 4], [8, 5, 6], [4, 2, 6, 2], [1, 5, 2, 3, 4]]
print(solution(triangle))