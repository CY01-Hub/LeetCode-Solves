# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        ans = []
        if root is None:
            return ans

        elif root.left is None and root.right is None:
            ans.append(str(root.val))
            return ans

        left = self.binaryTreePaths(root.left)
        right = self.binaryTreePaths(root.right)

        for l in left:
            ans.append(str(root.val) + "->" + str(l))
        
        for r in right:
            ans.append(str(root.val) + "->" + str(r))

        return ans