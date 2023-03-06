# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root) -> bool:
        return self.validate(root,float("-inf"),float("inf"))

    def validate(self,node,min_val,max_val):
        if not node:
            return True
        
        if not (min_val < node.val < max_val):
            return False
        
        return self.validate(node.left,min_val,node.val) and self.validate(node.right,node.val,max_val)
    def print_tree(self, root):
        arr =[]
        queue = [root]
        while queue:
            root = queue.pop(0)
            arr.append(root.val)
            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)
        return arr
    


#[5,4,6,null,null,3,7]
if __name__ == "__main__":
    s = Solution()
    root = TreeNode(2,TreeNode(2),TreeNode(2))
    print(s.print_tree(root=root))
    print(s.isValidBST(root=root))