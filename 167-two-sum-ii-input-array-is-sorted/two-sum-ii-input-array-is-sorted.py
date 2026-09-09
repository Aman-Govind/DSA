class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
       dt={}
       for i in range(len(numbers)):
        comp=target-numbers[i]
        if comp in dt:
            return [dt[comp]+1,i+1]
        dt[numbers[i]]=i