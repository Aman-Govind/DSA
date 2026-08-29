class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer=[]
        list1=set()
        list2=set()
        for i in nums1:
            if i not in nums2:
                list1.add(i)
        answer.append(list(list1))
        for i in nums2:
            if i not in nums1:
                list2.add(i)
        answer.append(list(list2))
        return answer