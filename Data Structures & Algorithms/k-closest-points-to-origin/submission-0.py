class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        max_heap = []

        for x,y in points:
            dist = -(x**2 + y**2)

            heapq.heappush(max_heap, [dist, x, y])

            if len(max_heap) > k:
                heapq.heappop(max_heap)

        res = []
        while max_heap:
            value = max_heap.pop()
            res.append([value[1],value[2]])

        return res