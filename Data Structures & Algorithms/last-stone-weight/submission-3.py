class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # x==y -> pop x, pop y
        # x < y -> pop x, pop y -> push y-x

        max_heap = []
        
        for s in stones:
            heapq.heappush(max_heap, -s)
        
        while len(max_heap) > 1:
            y = -heapq.heappop(max_heap)    #largest
            x = -heapq.heappop(max_heap)    # second largest

            if x != y:
                heapq.heappush(max_heap, -(y-x))

        if len(max_heap) == 0:
            return 0
        
        return -max_heap[0]