class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        res = []
        tracker = {}

        for n in nums:
            if n in tracker:
                tracker[n] += 1
            else:
                tracker[n] = 1
        
        while k:
            res.append(max(tracker, key=tracker.get))
            tracker.pop(max(tracker, key=tracker.get))
            k -= 1

        return res

        
        # create a tracker {} storing frequencies
        # if n exists: increment
        # else: add with val = 1
        # loop through and find res

