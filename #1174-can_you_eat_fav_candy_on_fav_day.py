class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(candiesCount)
        answer = [False] * len(queries)
        
        prefixSum = [0] * n
        prefixSum[0] = candiesCount[0]
        for i in range(1, n):
            prefixSum[i] = prefixSum[i - 1] + candiesCount[i]

        for i in range(len(queries)):
            favoriteType = queries[i][0]
            favoriteDay = queries[i][1]
            dailyCap = queries[i][2]
            
            minCandiesNeeded = favoriteDay + 1
            maxCandiesEaten = (favoriteDay + 1) * dailyCap
            
            candiesStart = 1 if favoriteType == 0 else prefixSum[favoriteType - 1] + 1
            candiesEnd = prefixSum[favoriteType]

            answer[i] = not (minCandiesNeeded > candiesEnd or maxCandiesEaten < candiesStart)

        return answer
