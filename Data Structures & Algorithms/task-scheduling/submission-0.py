class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        
        # track of how many more tasks to be done before reuse same task/letter
        # task seqeunce: each unique letter once, then check how many idles needed via first letter, then repeat
        # use most freq letter first
        # maxheap to store most freq letter
        tasks_counter = Counter(tasks)
        heap = []
        for task, count in tasks_counter.items():
            heap.append((-count, task))
        heapq.heapify(heap)

        # ["A","A","A", "B","B","B"], n=3 -> {A:3, B:3} -> {A:2, B:3}
        intervals = 0                        # A->idle->idle   
        cooldown = deque()     
        while heap or cooldown:
            intervals += 1
            
            if heap:
                negative_count, task = heapq.heappop(heap)
                negative_count += 1 #neg because maxheap, daher auch += statt -=

                if negative_count < 0:
                    available_time = intervals + n 
                    cooldown.append((available_time, negative_count, task)) #eg (4, -2, "A")

             # entferne ch so lange von maxheap mit ch wieder teil der seq sein kann (wieder im heap ist/gepusht wurde)
            if cooldown and (cooldown[0][0] <= intervals):
                available_time, negative_count, task = cooldown.popleft()
                heapq.heappush(heap, (negative_count, task))

        return intervals
