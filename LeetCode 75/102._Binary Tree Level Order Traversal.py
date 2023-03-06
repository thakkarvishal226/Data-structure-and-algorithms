# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root):
        queue = [root] if root else []
        res = []
        while queue:
            levels = []
            l = len(queue)
            for _ in range(l):
                node = queue.pop(0)
                levels.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(levels)
        return res



if __name__ == "__main__":
    s = Solution()
    root = TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))
    print(s.levelOrder(root=root))