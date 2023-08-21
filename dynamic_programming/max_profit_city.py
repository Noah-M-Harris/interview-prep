def solution(cityA, cityB):

    dp = [[0] * (len(cityA) + 2) for _ in range(len(cityB) + 2)]
    
    city_b_sum = 0
    for r in range(len(cityA) -1, -1, -1):
        city_a_sum = 0
        city_b_sum += cityB[r]
        for c in range(len(cityB) -1, -1, -1):
            city_a_sum += cityA[c]
            dp[r][c] = max(city_a_sum, city_b_sum, cityA[c] + dp[r + 2][c + 2])

    print(dp)
    return dp[0][0]


print(solution([4, 3, 5], [1, 2, 12]))
print(solution([4, 3, 5], [1, 1, 1]))