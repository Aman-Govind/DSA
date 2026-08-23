class Solution:
    def defangIPaddr(self, address: str) -> str:
        substring=""
        for i in address:
            if i==".":
                substring+="[.]"
            else:
                substring+=i
        return substring