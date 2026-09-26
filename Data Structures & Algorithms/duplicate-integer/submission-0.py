class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x = {}
        n = len(nums)

        for num in nums:
            x[num] = x.get(num, 0) + 1
        
        for num in x:
            if x[num] > 1:
                return True
        return False
        