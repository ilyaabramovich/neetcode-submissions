class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for idx, num in enumerate(nums):
            if num in d:
                return [d[num], idx]
            d[target-num] = idx

        