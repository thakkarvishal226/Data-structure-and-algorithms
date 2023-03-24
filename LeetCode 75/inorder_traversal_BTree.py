# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, rootTreeNode):
        result = []
        stack = [rootTreeNode]
        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            result.append(node.val)
            
            
            
            if node.left:
                stack.append(node.left)

            
        return result

if __name__ == "__main__":
    s =Solution()
    root = TreeNode(5,TreeNode(3,TreeNode(2),TreeNode(4)),TreeNode(8,TreeNode(6),TreeNode(9)))
    print(s.inorderTraversal(root))
