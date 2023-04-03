# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p, q):
        stack = []
        if p and q:
            stack.append((p,q))
        elif p:
            stack.append((p,None))
        elif q:
            stack.append((None, q))
        while stack:
            p, q = stack.pop()
            if (p and not q) or (not p and q):
                return False
            elif (p.left and not q.right) or (not p.left and  q.right):
                return False
            elif (p.right and not q.left) or (not p.right and  q.left):
                return False
            elif p.val != q.val:
                return False
            
            if p.left and q.right:
                stack.append((p.left,q.right))
            if p.right and q.left:
                stack.append((p.right,q.left))
        return True
    def isSymmetric(self, root) -> bool:
        return self.isSameTree(root.left,root.right)


if __name__ == "__main__":
    #[9,-42,-42,null,76,76,null,null,13,null,13]
    root = TreeNode(9,TreeNode(-42,None,TreeNode(76,None,TreeNode(13))),TreeNode(-42,TreeNode(76,None,TreeNode(13)),None))
    s = Solution()
    print(s.isSymmetric(root=root))
    