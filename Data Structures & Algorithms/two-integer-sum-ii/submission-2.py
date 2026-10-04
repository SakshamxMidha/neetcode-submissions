class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = defaultdict(set)


        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in x:
                return [x[diff] + 1,i + 1]

            x[nums[i]] = i





        