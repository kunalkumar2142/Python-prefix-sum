class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        sum_ = 0 # sum is a keyword in Python, so using sum_
        for i in range(left, right + 1):
            sum_ += self.nums[i]
        return sum_
