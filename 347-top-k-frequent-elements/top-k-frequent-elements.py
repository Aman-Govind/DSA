class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        list1=list(set(nums))
        count=[]
        for i in list1:
            count.append(nums.count(i))
        ans=[]
        for j in range(k):
            i=max(count)
            index=count.index(i)
            ans.append(list1[index])
            count[index]=0
        return ans
