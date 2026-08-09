class Solution:
    def reverseWords(self, s: str) -> str:
        list1=s.split()
        list2=list1[::-1]
        substring=list2[0]
        for i in list2[1:]:
            substring+=" "+i
        return substring