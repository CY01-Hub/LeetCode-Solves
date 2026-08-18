# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if root == None:
            return None
        current = root
        while current != None:
            if current.val == target:
                return current
            elif current.val > target:
                current = current.left
            else:
                current = current.right
        
        return None