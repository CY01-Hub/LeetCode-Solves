# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        if head.next is None:
            return True

        slow, fast = head, head
        stack = []

        while fast and fast.next is not None:
            stack.append(slow.val)
            slow, fast = slow.next, fast.next.next
        
        if fast:
            slow = slow.next
        
        while slow:
            if slow.val != stack.pop():
                return False
            slow = slow.next
        
        return True