# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root) -> int:
        def traversal(node,pathvalue,totalvalue):
            if not node:
                return 0 
            pathvalue = pathvalue *10 + node.val
            if (node.left == None and node.right == None):
                return pathvalue
            
            leftval = traversal(node.left,pathvalue,totalvalue)
            rightval = traversal(node.right,pathvalue,totalvalue)
            
            total = leftval + rightval
            
            return total
        return traversal(root, 0, 0)



if __name__ == "__main__":
    s =Solution()
    root = TreeNode(4,TreeNode(9,TreeNode(5),TreeNode(1)),TreeNode(0))
    print(s.sumNumbers(root))