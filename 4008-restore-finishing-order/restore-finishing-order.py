class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        list1=[]
        for i in order:
            if i in friends:
                list1.append(i)
        return list1