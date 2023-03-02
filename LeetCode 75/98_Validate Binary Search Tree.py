# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root) -> bool:
        queue  = [root]
        while queue:
            currntnode = queue.pop(0)
            if currntnode.left and currntnode.right:
                if (currntnode.left.val < currntnode.val < currntnode.right.val):
                    queue.append(currntnode.left)
                    queue.append(currntnode.right)
                else:
                    return False
            elif currntnode.left:
                if (currntnode.left.val < currntnode.val):
                    queue.append(currntnode.left)
                else:
                    return False
            elif currntnode.right:
                if (currntnode.val < currntnode.right.val):
                    queue.append(currntnode.right)
                else:
                    return False
        return True
    


#[5,4,6,null,null,3,7]
if __name__ == "__main__":
    s = Solution()
    root = TreeNode(5,TreeNode(4),TreeNode(6,TreeNode(3),TreeNode(7)))
    print(s.isValidBST(root=root))