class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        base={}
        for i in knowledge:
            base[i[0]]=i[1]
        ans=""
        i=0
        while i<len(s):
            if s[i]=="(":
                j=i+1
                while s[j]!=")":
                    j+=1
                string=s[i+1:j]
                if string in base:
                    ans+=base[string]
                else:
                    ans+="?"
                i=j+1
            else:
                ans+=s[i]
                i+=1
        return ans