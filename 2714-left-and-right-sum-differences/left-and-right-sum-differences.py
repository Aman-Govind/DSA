class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        list1=[]
        list2=[]
        list3=[]
        a=0
        for i in nums:
            list1.append(a)
            a+=i
        b=0
        for i in range(len(nums)-1,-1,-1):
            list2.append(b)
            b+=nums[i]
        list2=list2[::-1]
        for i in range(len(nums)):
            list3.append(abs(list1[i]-list2[i]))
        return list3
