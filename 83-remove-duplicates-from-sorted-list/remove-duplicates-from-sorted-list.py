# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        temp = -101

        prev, curr = None, head
        while curr:
            if curr.val == temp:
                prev.next = curr.next
            else:
                temp = curr.val
                prev = curr
            curr = curr.next
        
        return head