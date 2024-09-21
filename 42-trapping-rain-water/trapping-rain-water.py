class Solution:
    def trap(self, height: List[int]) -> int:
        
        # make note when finding index that's smaller than curr
        # make sure there is height >= curr height so water can be trapped
        # keep track of distance between two heights to calc area
        # for height[i] -> find "boundaries" > height[i] (before and after)

        # i = 5, h = 1
        # l = 2, r = 3 -> area = min(l, r) - h = 1
        # l, r to keep track of heights 

        # i = 6, h = 0
        # l = 2, r = 3 -> area = min(l , r) - h = 2

        # i = 7, h =1
        # l = 2, r = 3 -> 2 - 1 = 1

        # check if l and r boundaries exist
        # if not, continue to next

        # maxL, maxR = 0, 0
        l = height[0]
        r = height[len(height) - 1]
        maxR = [0] * len(height)
        for i in range(len(height) - 1, -1, -1):
            r = max(r, height[i])
            maxR[i] = r
        
        total = 0

        for i in range(1, len(height)):
            l = max(l, height[i])
            r = maxR[i]

            if l < height[i] or r < height[i]:
                continue
            total += min(l, r) - height[i]

        return total
