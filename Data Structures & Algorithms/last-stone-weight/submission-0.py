class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]

        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            first_stone = -heapq.heappop(heap)
            second_stone = -heapq.heappop(heap)

            if first_stone != second_stone:
                diff = first_stone - second_stone
                heapq.heappush(heap, -diff)
                
        if len(heap) == 1:
            return -heap[0]
        return 0
