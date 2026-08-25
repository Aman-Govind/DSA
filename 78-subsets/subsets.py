class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def sol(i,current):
            if i==len(nums):
                res.append(current)
                return
            sol(i+1,current)
            sol(i+1,current+[nums[i]])
        sol(0,[])
        return res