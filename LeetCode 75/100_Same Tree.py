# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p, q) -> bool:
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
            elif (p.left and not q.left) or (not p.left and  q.left):
                return False
            elif (p.right and not q.right) or (not p.right and  q.right):
                return False
            elif p.val != q.val:
                return False
            
            if p.left and q.left:
                stack.append((p.left,q.left))
            if p.right and q.right:
                stack.append((p.right,q.right))
        return True


if __name__ == "__main__":
    s = Solution()
    p = TreeNode(1,TreeNode(4),TreeNode(3))
    q = TreeNode(0)
    print(s.isSameTree(None, q))
