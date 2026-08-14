class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        list1=[]
        for i in matrix:
            list1.append(sum(i))
        return list1