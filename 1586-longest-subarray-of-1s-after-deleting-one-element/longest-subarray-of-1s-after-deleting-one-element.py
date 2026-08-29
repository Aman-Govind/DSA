class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left=0
        zerCount=0
        maxcount=0
        for right in range(len(nums)):
            if nums[right]==0:
                zerCount+=1
            while zerCount>1:
                if nums[left]==0:
                    zerCount-=1
                left+=1
            maxcount=max(maxcount,right-left)
        return maxcount