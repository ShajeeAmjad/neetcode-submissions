class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # brute force
        # for i in range(len(numbers)):
        #     for j in range(len(numbers)):
        #         if numbers[i] + numbers[j] == target and i != j:
        #             return [i+1, j+1]
        
        # optimal solution
        l, r = 0, len(numbers)-1

        while l < r:

            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            
            while numbers[l] + numbers[r] > target and r > l:
                r -= 1
            while numbers[l] + numbers[r] < target and l < r:
                l += 1
            
                