class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        list1=[0]
        for i in gain:
            list1.append(list1[-1]+i)
        return max(list1)
