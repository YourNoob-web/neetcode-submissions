class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum = {}
        for i, n in enumerate(nums):
            compcent = target - n
            if compcent in sum:
                return [sum[compcent], i]
            sum[n] = i 
        