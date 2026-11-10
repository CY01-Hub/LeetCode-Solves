# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, k, count):
        if root is None:
            return None

        left = self.helper(root.left, k, count)

        if left is not None:
            return left

        count[0] += 1

        if count[0] == k:
            return root.val

        return self.helper(root.right, k, count)

    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        count = [0]
        return self.helper(root, k, count)