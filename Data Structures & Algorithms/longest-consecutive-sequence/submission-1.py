class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        start = 0

        nums_set = set(nums)

        for i in range(len(nums)):
            if nums[i] - 1 in nums_set:
                continue

            k = 1
            while nums[i] + k in nums_set:
                k += 1

            res = max(res, k)
        return res