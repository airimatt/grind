class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        # iterate backwards
        # if nums[i] == val:
        # 1: if i == len(nums) - 1: nums.pop()
        # 2: else: swap with elt at end and then pop the end

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                if i == len(nums) - 1:
                    nums.pop()
                else:
                    temp = nums[len(nums) - 1]
                    nums[len(nums) - 1] = nums[i]
                    nums[i] = temp
                    nums.pop()

        return len(nums)


        