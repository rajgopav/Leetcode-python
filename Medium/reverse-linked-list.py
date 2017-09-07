class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))

class Solution(object):
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        curr = head
        prev = None
        nxt = None
        while (curr != None):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print Solution().reverseList(head)
