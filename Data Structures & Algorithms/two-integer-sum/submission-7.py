class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # brute force
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if nums[i] + nums[j] == target and i != j:
        #             return [i, j]
        
        # optimal
        hash_map = {}
        for i, n in enumerate(nums):
            difference = target - n
            if difference in hash_map:
                return [hash_map[difference], i]
            else:
                hash_map[n] = i
            
            
        