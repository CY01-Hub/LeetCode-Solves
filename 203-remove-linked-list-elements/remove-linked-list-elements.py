# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], target: int) -> Optional[ListNode]:
        p = ListNode(0)
        p.next = head

        q = p
        while q.next:
            if q.next.val == target:
                q.next = q.next.next
            else:
                q = q.next
                
        return p.next
                