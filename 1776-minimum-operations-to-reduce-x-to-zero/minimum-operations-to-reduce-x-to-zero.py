class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target=sum(nums)-x
        left=0
        cursum=0
        maxlen=-1
        for right in range(len(nums)):
            cursum+=nums[right]
            while cursum>target and left<=right:
                cursum-=nums[left]
                left+=1
            if cursum==target:
                   maxlen=max(maxlen,right-left+1) 
        if maxlen==-1:
            return -1
        return len(nums)-maxlen