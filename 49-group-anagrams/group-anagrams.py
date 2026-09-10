class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        order={}
        for i in strs:
            key="".join(sorted(i))
            if key not in order:
                order[key]=[]
            order[key].append(i)
        return list(order.values())
      