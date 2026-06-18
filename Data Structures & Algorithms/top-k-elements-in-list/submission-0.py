class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hmap = {}

        for i in nums:
            if i in hmap:
                hmap[i] += 1
            else:
                hmap[i] = 1
            
        max_heap = []
        heapq.heapify(max_heap)

        for i in hmap:
            freq = hmap[i]
            heapq.heappush(max_heap, [-freq, i])

        res = []
        for i in range(k):
            number = heapq.heappop(max_heap)
            res.append(number[1])

        return res