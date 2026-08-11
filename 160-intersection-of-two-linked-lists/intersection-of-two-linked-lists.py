# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p = headA
        q = headB
        c = 0

        while True:
            if p == q:
                return p

            p = p.next
            q = q.next
            
            if p == None:
                c += 1
                p = headB

            if q == None:
                q = headA

            if c == 2:
                return None