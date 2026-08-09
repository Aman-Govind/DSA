class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        stack=[]
        count=[]
        for i in nums:
            if stack and stack[-1]==i:
                count[-1]+=1
            else:
                stack.append(i)
                count.append(1)
            if count[-1]>2:
                count[-1]=2
        list1=[]
        for i in range(len(stack)):
            for j in range(count[i]):
                list1.append(stack[i])
        nums[:]=list1
        return len(list1)