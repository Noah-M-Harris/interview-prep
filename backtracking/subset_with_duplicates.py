def solution(arr):
    """ 
    given a list of nums that are not necessarily distinct
    return all distinct subsets
    """

    """ sort input, run backtrack skip i while it is same as i-1 """
    arr.sort()

    def dfs(i, path, paths):

        """ invalid base case """
        if i >= len(arr):
            paths.append(path[:])
            return
        
        """ consider the cases for i """
        path.append(arr[i])
        dfs(i + 1, path, paths)
        path.pop() 

        while (i + 1) < len(arr) and arr[i] == arr[i+1]:
            i += 1
        
        dfs(i + 1, path, paths)

    paths = []
    dfs(0, [], paths)
    return paths

arr = [1, 3, 2, 2]
print(solution(arr))