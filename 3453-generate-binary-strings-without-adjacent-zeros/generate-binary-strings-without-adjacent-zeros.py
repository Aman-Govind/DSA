class Solution:
    def validStrings(self, n: int) -> List[str]:
        res=[]
        def ans(s):
            if len(s)==n:
                res.append(s)
                return
            ans(s+"1")
            if len(s)==0 or s[-1]=="1":
                ans(s+"0")
        ans("")
        return res
