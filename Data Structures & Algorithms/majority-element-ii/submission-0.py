class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        m = len(nums)
        n = m//3
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        elem = [key for key in freq if freq[key] > n]
        return elem


        