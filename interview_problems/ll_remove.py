class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        new_head = pre = ListNode(0)
        pre.next = head
        
        while head:
            if head.val == val:
                pre.next = head.next
            else:
                pre = pre.next
            head = head.next
        return new_head.next
    
# time complexity of this soltuion is  O(1) linear
    
    