class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars)==1:
            return 1
        res=[]
        stack=[chars[0]]
        for i in chars[1:]:
            if stack[-1]==i:
                stack.append(i)
            else:
                char=stack[0]
                res.append(char)
                if len(stack)>1:
                    res+=list(str(len(stack)))
                stack=[i]
        ch=stack[0]
        res.append(ch)
        if len(stack)>1:
            res+=list(str(len(stack)))
        chars[:]=res