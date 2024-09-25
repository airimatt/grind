class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while stones:
            if len(stones) < 2:
                return stones[0] * -1

            # y = stones[0]
            # x = stones[1]

            y = heapq.heappop(stones)
            x = heapq.heappop(stones)
            # print(x, y)

            if x != y:
                # print(y - x)
                heapq.heappush(stones, y - x)

            # heapq.heappop(stones)
            # heapq.heappop(stones)
            

            # for s in stones:
            #     print(s)
            # print("---")


        return 0
        