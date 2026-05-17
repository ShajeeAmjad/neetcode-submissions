class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # brute force
        result = []
        for i in range(len(nums)):
            excluded_index = i
            product = 1
            for j in range(len(nums)):
                if j != excluded_index:
                    product *= nums[j]
            result.append(product)
        return result

        
                