class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack=[]
        count=[]
        for i in s:
            if stack and stack[-1]==i:
                count[-1]+=1
            else:
                stack.append(i)
                count.append(1)
            if count[-1]==k:
                stack.pop()
                count.pop()
        substring=""
        for i in range(len(stack)):
            substring+=stack[i]*count[i]
        return substring