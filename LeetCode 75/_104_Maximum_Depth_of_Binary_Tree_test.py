import unittest
import _104_Maximum_Depth_of_Binary_Tree as entity


class TestTree(unittest.TestCase):
    def test_depth(self):
        self.assertEqual(entity.Solution().maxDepth(None),0)
        self.assertEqual(entity.Solution().maxDepth(root=entity.TreeNode(0)),1)
        self.assertEqual(entity.Solution().maxDepth(root=entity.TreeNode(1,entity.TreeNode(2),entity.TreeNode(3))),2)
        self.assertEqual(entity.Solution().maxDepth(root=entity.TreeNode(1,entity.TreeNode(2),entity.TreeNode(3,entity.TreeNode(5,entity.TreeNode(6))))),4)



if __name__ == "__main__":
    unittest.main()