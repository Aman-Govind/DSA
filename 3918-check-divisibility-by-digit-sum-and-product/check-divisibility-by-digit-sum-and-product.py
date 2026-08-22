class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sum=0
        pro=1
        for i in str(n):
            sum+=int(i)
            pro*=int(i)
        return n%(sum+pro)==0