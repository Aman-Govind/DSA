# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(x,y):
            if x==0:
                return y
            return gcd(y%x,x)
        current=head
        if not head or not head.next:
            return head
        while current.next:
            ans=gcd(current.val,current.next.val)
            ansNode=ListNode(ans)
            ansNode.next=current.next
            current.next=ansNode
            current=ansNode.next
        return head

