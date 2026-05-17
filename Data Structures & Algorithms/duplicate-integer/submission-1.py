class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # hmap = {}
        # count = 0

        # for num in nums:
        #     if not hmap:
        #         hmap = hmap.add(num)
        #         count += 1
        #         hmap[num] = count

        # brute force solution
        for i in range(len(nums)):
            num = nums[i]
            for j in range(len(nums)):
                if num == nums[j] and i != j:
                    return True
        return False

            
        