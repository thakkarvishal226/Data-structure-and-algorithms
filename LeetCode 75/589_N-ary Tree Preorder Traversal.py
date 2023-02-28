# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node'):
        arr = [root]
        out = []
        node  = arr.pop(0)
        while node:
            out.append(node.val)
            if node.children:
                arr = node.children + arr 
            node = arr.pop(0) if len(arr) > 0 else None
        return out

    
if __name__ == "__main__":
    s = Solution()
    input_data = Node(1,[Node(3,[Node(5),Node(6)]),Node(2),Node(4)])
    print(s.preorder(input_data))