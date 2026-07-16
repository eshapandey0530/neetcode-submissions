class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        # task X time = 1, next X == time + n = 1 + n
        # else: idle
        # minheap - to get the elements with least frequency to top
        # keep record of tasks left and at what time
        # create hmap with frequency count

        minheap = []
        taskq = deque()
        hmap = {}

        for task in tasks:
            if task in hmap:
                hmap[task] += 1
            else:
                hmap[task] = 1

        for t in hmap:
            freq = hmap[t]
            heapq.heappush(minheap, [-freq, t])

        time = 0

        while minheap or taskq:

            time += 1

            if minheap:
                task = heapq.heappop(minheap)   #[-3,A]
                if task[0] < -1: # taskq = [[-2, 4, A]]
                    taskq.append([task[0] + 1, time + n, task[1]])

            while taskq and taskq[0][1] <= time:
                new_task = taskq.popleft()
                if new_task[0] < 0:
                    freq, task = new_task[0], new_task[2]
                    heapq.heappush(minheap, [freq, task])

        return time



