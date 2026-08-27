class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        list1=[]
        for i in nums:
            list1.append(int(i)*-1)
        heapq.heapify(list1)
        for i in range(k-1):
            heapq.heappop(list1)
        return str(-heapq.heappop(list1))