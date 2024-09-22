class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.stream = []
        nums.sort()
        for n in nums:
            self.stream.append(n)
        

    def add(self, val: int) -> int:
        # need to do binary search and add element where it belongs in stream
        # return elt at index k - 1
        self.stream.append(val)
        self.stream.sort()
        return self.stream[len(self.stream) - self.k]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)