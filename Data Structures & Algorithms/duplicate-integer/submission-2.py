class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # brute force solution
        for i in range(len(nums)):
            num = nums[i]
            for j in range(len(nums)):
                if num == nums[j] and i != j:
                    return True
        return False

            
        