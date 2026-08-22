class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seen=[0]*(len(A)+1)
        ans=[]
        common=0
        for i in range(len(A)):
            seen[A[i]]+=1
            if seen[A[i]]==2:
                common+=1
            seen[B[i]]+=1
            if seen[B[i]]==2:
                common+=1
            ans.append(common)
        return ans
