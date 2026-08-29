# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count=0
        temp=head
        while temp:
            count+=1
            temp=temp.next
        counter=0
        current=head
        if count==1:
            return 
        while counter!=count//2-1:
            counter+=1
            current=current.next
        current.next=current.next.next
        return head