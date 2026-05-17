class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 1. Handle the empty list case first
        if not nums:
            return 0
        
        longest_streak = 0
        
        # 2. For every number in the list...
        for num in nums:
            current_num = num
            current_streak = 1
            
            # 3. While the NEXT number exists in our list, 
            # keep incrementing and counting.
            while (current_num + 1) in nums:
                current_num += 1
                current_streak += 1
            
            # 4. Update our record if this streak was longer than the last
            if current_streak > longest_streak:
                longest_streak = current_streak
                
        return longest_streak