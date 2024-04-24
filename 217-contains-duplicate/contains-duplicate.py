class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # nums.sort()
        # for i in range(len(nums) - 1):
        #     if (nums[i] == nums[i + 1]): return True

        # return False 
        
        hashTable = set()

        for n in nums:
            if n in hashTable: return True
            hashTable.add(n)
        
        return False