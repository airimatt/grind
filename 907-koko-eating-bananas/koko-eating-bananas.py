class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        k = r

        while l <= r:
            mid = (l + r) // 2
            time = 0
            for p in piles:
                time += math.ceil(float(p) / mid)
            if time <= h:
                k = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return k



        # while l <= r:
        #     k = (l + r) // 2

        #     totalTime = 0
        #     for p in piles:
        #         totalTime += math.ceil(float(p) / k)
        #     if totalTime <= h:
        #         res = k
        #         r = k - 1
        #     else:
        #         l = k + 1
        # return res