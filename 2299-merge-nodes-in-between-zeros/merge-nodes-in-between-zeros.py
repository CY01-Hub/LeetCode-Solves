# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(-1)
        ans = dummy
        curr = head.next
        add = 0

        while curr != None:
            if curr.val != 0:
                add += curr.val
            else:
                temp = ListNode(add)
                dummy.next = temp
                dummy = dummy.next
                add = 0
            curr = curr.next

        return ans.next