# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root):
        queue = [root]
        res = []
        while queue:
            levels = []
            l = len(queue)
            for _ in range(l):
                node = queue.pop()
                levels.append(node.val)
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
            res.append(levels)
        return res



if __name__ == "__main__":
    s = Solution()
    root = TreeNode(1,TreeNode(2),TreeNode(3,TreeNode(4),TreeNode(5)))
    print(s.levelOrder(root=root))