# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        tracker = set()

        prev, curr = None, head
        while curr:
            if curr.val in tracker:
                prev.next = curr.next
            else:
                tracker.add(curr.val)
                prev = curr
            curr = curr.next
        
        return head