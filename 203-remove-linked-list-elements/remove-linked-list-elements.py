# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], target: int) -> Optional[ListNode]:
        if head is None:
            return None

        dummy = ListNode(-1)
        dummy.next = head
        curr = dummy

        while curr.next != None:
            if curr.next.val == target:
                curr.next = curr.next.next
            else:
                curr = curr.next
        
        return dummy.next
                