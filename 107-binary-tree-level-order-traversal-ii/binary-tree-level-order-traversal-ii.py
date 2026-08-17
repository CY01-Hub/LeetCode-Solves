# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Queue:
    def __init__(self):
        self.q = []
        self.front = -1

    def push(self, x):
        if self.front == -1:
            self.front = 0
        self.q.append(x)

    def pop(self):
        if len(self.q) == 0:
            return -1
        else:
            x = self.q[self.front]
            self.front += 1
            if self.front == len(self.q):
                self.front = -1
                self.q = []
            return x

    def getFront(self):
        if len(self.q) == 0:
            return -1
        return self.q[self.front]

    def size(self):
        if self.front == -1:
            return 0
        return len(self.q) - self.front

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        ans = []

        if root is None:
            return ans

        q = Queue()
        q.push(root)

        while q.size() > 0:
            l = q.size()
            level = []

            for _ in range(l):
                front = q.pop()
                level.append(front.val)

                if front.left:
                    q.push(front.left)

                if front.right:
                    q.push(front.right)

            if len(level) > 0:
                ans.append(level)

        ans.reverse()
        return ans

