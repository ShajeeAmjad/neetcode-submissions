class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # brute force
        new = nums1 + nums2
        new = sorted(new)
        if len(new) % 2 == 0:
            mid = len(new) // 2 - 1
            temp = mid + 1
            median = (new[mid] + new[temp]) / 2
        else:
            mid = len(new) // 2
            median = new[mid]

        return median