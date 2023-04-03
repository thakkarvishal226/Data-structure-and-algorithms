# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root) -> int:
        if not root:
            return 0
        
        return max(self.maxDepth(root.left),self.maxDepth(root.right)) + 1


if __name__ == "__main__":
    #root=TreeNode(1,TreeNode(2),TreeNode(3,TreeNode(5,TreeNode(6))))
    root = TreeNode(0)
    s = Solution()
    print(s.maxDepth(root))