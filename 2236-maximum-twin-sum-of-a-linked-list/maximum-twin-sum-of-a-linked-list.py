# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        count=0
        temp=head
        res=[]
        while temp:
            res.append(temp.val)
            temp=temp.next
        sumnode=[]
        left=0
        right=len(res)-1
        while left<right:
            sumnode.append(res[left]+res[right])
            left+=1
            right+=-1
        return max(sumnode)
            