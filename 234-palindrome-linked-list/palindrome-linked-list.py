# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        ans = []
        curr = head
        
        while curr != None:
            ans.append(curr.val)
            curr = curr.next
        
        ptr = head
        while ptr != None:
            if ans[-1] != ptr.val:
                return False
            ptr = ptr.next
            ans.pop()
        
        return True