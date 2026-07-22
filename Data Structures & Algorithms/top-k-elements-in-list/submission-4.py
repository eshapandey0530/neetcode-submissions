class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)

        count_map = {}

        for num in nums:
            if num in count_map:
                count_map[num] += 1
            else:
                count_map[num] = 1

        bucket = [[] for i in range(n+1)]

        for key in count_map:
            count = count_map[key]
            bucket[count].append(key)

        print(bucket)

        res = []

        for i in range(n, 0, -1):
            j = 0
            while j < len(bucket[i]) and k != 0:
                res.append(bucket[i][j])
                j += 1
                k -= 1
        
        return res

        '''using hashmap and minHeap, keeping the size of minheap limited to 
        k, time complexity - O(n + log k), space - n
        '''        
        # hashmap = {}

        # for num in nums:
        #     if num in hashmap:
        #         hashmap[num] += 1
        #     else:
        #         hashmap[num] = 1

        # minHeap = []
        # heapq.heapify(minHeap)

        # result = []

        # for key in hashmap:
        #     freq = hashmap[key]
        #     heapq.heappush(minHeap, [freq, key])

        #     if len(minHeap) > k:
        #         heapq.heappop(minHeap)

        # for val in minHeap:
        #     num = val[1]
        #     result.append(num)

        # return result            
