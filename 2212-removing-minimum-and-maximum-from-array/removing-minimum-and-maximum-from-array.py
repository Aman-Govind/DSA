class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        maxi=max(nums)
        mini=min(nums)
        
        indexmax=nums.index(maxi)
        indexmin=nums.index(mini)

        left=max(indexmax,indexmin)+1

        right=len(nums)-min(indexmin,indexmax)

        both=(min(indexmin,indexmax)+1)+(len(nums)-max(indexmin,indexmax))
        return min(left,right,both)