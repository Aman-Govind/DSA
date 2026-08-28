class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
       hashmap={}
       count=0
       for i in nums:
        num=k-i
        if hashmap.get(num,0)>0:
            count+=1
            hashmap[num]-=1
        else:
            hashmap[i]=hashmap.get(i,0)+1
       return count