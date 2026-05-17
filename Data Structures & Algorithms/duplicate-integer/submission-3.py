class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # brute force solution
        # for i in range(len(nums)):
        #     num = nums[i]
        #     for j in range(len(nums)):
        #         if num == nums[j] and i != j:
        #             return True
        # return False

        # optimal solution
        hash_map = {}
        count = 0
        for num in nums:
            if hash_map.get(num, 0):
                return True
            else:
                count += 1
                hash_map[num] = count
            count = 0
            print(hash_map)
        return False

            
        