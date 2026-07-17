class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashmap = {}

        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1

        minHeap = []
        heapq.heapify(minHeap)

        result = []

        for key in hashmap:
            freq = hashmap[key]
            heapq.heappush(minHeap, [freq, key])

            if len(minHeap) > k:
                heapq.heappop(minHeap)

        for val in minHeap:
            num = val[1]
            result.append(num)

        return result            
