# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        list1=[]
        temp=head
        while temp:
            list1.append(temp.val)
            temp=temp.next
        i=0
        res=[]
        while(i<len(list1)):
            temp=list1[i:i+k]
            if len(temp)==k:
                temp=temp[::-1]
            res=res+temp
            i+=k
        newhead=ListNode(res[0])
        temp=newhead
        for i in range(1,len(res)):
            temp.next=ListNode(res[i])
            temp=temp.next
        return newhead