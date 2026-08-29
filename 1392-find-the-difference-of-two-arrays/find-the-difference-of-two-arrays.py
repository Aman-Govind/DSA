class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer=[]
        list1=[]
        list2=[]
        for i in nums1:
            if i not in nums2:
                list1.append(i)
        answer.append(list(set(list1)))
        for i in nums2:
            if i not in nums1:
                list2.append(i)
        answer.append(list(set(list2)))
        return answer