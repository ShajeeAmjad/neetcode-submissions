class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            num = target - nums[i]
            if num in nums and nums.index(num) != i:
                return sorted([i, nums.index(num)])