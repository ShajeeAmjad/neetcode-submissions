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

        # prefix, postfix method
        result = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] = postfix
            postfix *= nums[i]
        return result



                