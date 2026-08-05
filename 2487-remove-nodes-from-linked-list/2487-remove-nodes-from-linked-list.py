# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverse(self, head):
        prev=None
        curr=head
        while curr:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        return prev    
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head=self.reverse(head)
        max_val=head.val
        curr=head
        while curr and curr.next:
            if curr.next.val<max_val:
                curr.next=curr.next.next
            else:
                curr=curr.next
                max_val=curr.val
        return self.reverse(head)            
        