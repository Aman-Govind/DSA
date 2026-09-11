class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        ans=set()
        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if i==k or j==k or i==j:
                        continue
                    if digits[i]==0:
                        continue
                    if digits[k]%2!=0:
                        continue
                    number=digits[i]*100+digits[j]*10+digits[k]
                    ans.add(number)
        return len(ans)