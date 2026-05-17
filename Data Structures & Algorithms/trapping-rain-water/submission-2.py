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

        # two pointers
        if not height:
            return 0
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res

            



        