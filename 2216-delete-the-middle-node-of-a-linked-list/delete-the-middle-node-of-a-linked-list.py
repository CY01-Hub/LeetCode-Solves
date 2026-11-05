# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        if head.next is None:
            return None
        
        fast = slow = ptr = head
        
        while fast != None and fast.next != None:
            ptr = slow
            slow = slow.next
            fast = fast.next.next
        
        ptr.next = ptr.next.next
        return head
