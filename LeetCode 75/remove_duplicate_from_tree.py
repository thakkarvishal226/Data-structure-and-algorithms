
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head):
        node = head
        while node:
            if node.next:
                if node.val == node.next.val:
                    node.next = node.next.next
                else:
                    node = node.next
            else:
                node = node.next
        return head
    

if __name__ == "__main__":
    head = ListNode(1,ListNode(1,ListNode(1)))
    s = Solution()
    print(s.deleteDuplicates(head=head))