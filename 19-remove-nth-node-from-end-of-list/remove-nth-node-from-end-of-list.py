# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        x = ListNode(0, head)
        s = x
        f = x

        for _ in range(n):
            f = f.next

        while f.next is not None:
            s = s.next
            f = f.next

        s.next = s.next.next

        return x.next