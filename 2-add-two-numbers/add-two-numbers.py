# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, h1: Optional[ListNode], h2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(0)
        cary = 0
        
        p = h1
        q = h2
        r = ans

        while p != None or q != None:
            total = cary
            cary = 0

            if p != None:
                total += p.val
                p = p.next

            if q != None:
                total += q.val
                q = q.next

            if total > 9:
                cary = 1
                total -= 10

            newNode = ListNode(total)
            r.next = newNode
            r = r.next
        
        if cary>0:
            newNode = ListNode(cary)
            r.next = newNode

        return ans.next