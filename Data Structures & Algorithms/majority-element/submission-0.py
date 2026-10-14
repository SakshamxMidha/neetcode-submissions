class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        x = {}

        for num in nums:
            x[num] = x.get(num, 0) + 1
        
        majority = max(x, key=x.get)
        return majority
        