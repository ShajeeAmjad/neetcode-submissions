class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        
        max_left = [0] * n
        current_max = 0
        for i in range(n):
            max_left[i] = current_max
            if height[i] > current_max:
                current_max = height[i]

        max_right = [0] * n
        current_max = 0
        for j in range(n - 1, -1, -1):
            max_right[j] = current_max
            if height[j] > current_max:
                current_max = height[j]
        
        min_lr = [0] * n
        for k in range(n):
            min_lr[k] = min(max_left[k], max_right[k])
        
        # height - min_lr
        total = 0
        for l in range(n):
            if min_lr[l] - height[l] < 0:
                continue
            else:
                total += (min_lr[l] - height[l])

        return total

        