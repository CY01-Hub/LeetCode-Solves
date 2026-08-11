# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p = headA
        q = headB

        a, b = 0, 0
        while p.next != None:
            a += 1
            p = p.next
        while q.next != None:
            b += 1
            q = q.next

        p = headA
        q = headB

        if a > b:
            while a > b:
                p = p.next
                a -= 1
        elif b > a:
            while b > a:
                q = q.next
                b -= 1

        while p != q:
            p = p.next
            q = q.next
        
        return p

            