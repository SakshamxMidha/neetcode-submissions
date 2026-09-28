class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        x = {}

        for num in nums:
            x[num] = x.get(num,0) + 1
        
        sorted_nums = sorted(x, key = x.get, reverse=True)

        return sorted_nums[:k]
        