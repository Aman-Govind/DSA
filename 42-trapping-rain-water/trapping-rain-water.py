class Solution:
    def trap(self, height: List[int]) -> int:
        maxleft=[0]*len(height)
        maxright=[0]*len(height)

        for i in range(1,len(height)):
            maxleft[i]=max(maxleft[i-1],height[i-1])
        for i in range(len(height)-2,-1,-1):
            maxright[i]=max(maxright[i+1],height[i+1])
        inter=[0]*len(height)
        for i in range(len(height)):
            inter[i]=min(maxleft[i],maxright[i])
        res=[0]*len(height)
        for i in range(len(height)):
            res[i]=max(res[i],inter[i]-height[i])
        return sum(res)