class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def sol(current,used):
            if len(current)==len(nums):
                res.append(current)
                return
            for j in range(len(nums)):
                if nums[j]not in used:
                    sol(current+[nums[j]],used+[nums[j]])
        sol([],[])
        return res
