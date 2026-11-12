class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum = {}
        for i, num in enumerate(nums):
            complment = target - num
            if complment in sum:
                return [sum[complment],i]
            sum[num] = i