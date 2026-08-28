class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        temp=s[:k]
        count=0
        maxcount=0
        for i in temp:
            if i in "aeiou":
                count+=1
        maxcount=count
        if maxcount==k:
            return k
        
        for i in range(1,len(s)-k+1):
            if s[i-1] in "aeiou":
                count-=1
            if s[i+k-1] in "aeiou":
                count+=1
            maxcount=max(count,maxcount)
            if maxcount==k:
                return k
        return maxcount

            