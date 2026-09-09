class Solution:
    def reverseBits(self, n: int) -> int:
        def tobin(n):
            res=""
            while n>0:
                digit=n%2
                res=str(digit)+res
                n=n//2
            return res
        a=tobin(n)
        
        a=a.zfill(32)
        b=a[::-1]
        return int(b,2)
        