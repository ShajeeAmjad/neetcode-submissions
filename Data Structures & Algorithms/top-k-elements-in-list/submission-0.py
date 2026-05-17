class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = Counter(nums)
        # min-heap of (count, num)
        heap = []
        for num, count in freq.items():
            if len(heap) < k:
                heapq.heappush(heap, (count, num))
            else:
                if count > heap[0][0]:
                    heapq.heapreplace(heap, (count, num))
        # Extract numbers from heap
        return [num for count, num in heap]
        
        

        