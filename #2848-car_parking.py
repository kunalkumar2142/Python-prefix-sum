class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        prefix = [0] * 102
        for car in nums:
            prefix[car[0]] += 1
            prefix[car[1] + 1] -= 1
        count = 0
        p_sum = 0
        for i in range(1, 102):
            p_sum += prefix[i]
            if p_sum > 0:
                count += 1
        return count
        
