class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def sol(i,current,total):
            if total==target:
                res.append(current)
                return 
            if total>target or i==len(candidates):
                return
            sol(i+1,current,total)
            sol(i,current+[candidates[i]],total+candidates[i])
        sol(0,[],0)
        return res