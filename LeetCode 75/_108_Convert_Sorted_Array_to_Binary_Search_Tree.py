# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums):
        pass



if __name__ == "__main__":
    s = Solution()
    mylist = [-10, -3, 0, 5, 9]
    s.printTree(s.sortedArrayToBST(mylist))