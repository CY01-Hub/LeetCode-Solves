# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = head.next
        curr = head

        while curr.next is not None:
            if curr.next.val == 0:
                curr.next = curr.next.next
                
                if curr.next is None:
                    break
                
                curr = curr.next
                continue
            
            newVal = curr.val + curr.next.val
            curr.next = curr.next.next
            curr.val = newVal
        
        return head
        