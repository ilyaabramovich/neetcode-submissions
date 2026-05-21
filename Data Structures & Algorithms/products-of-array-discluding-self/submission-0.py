class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix_left = [1]

        for num in nums:
            prefix_left.append(prefix_left[-1] * num)
        
        prefix_right = [1]

        for num in reversed(nums):
            prefix_right.append(prefix_right[-1] * num)
            last = prefix_right[-1]

        for i in range(1, len(prefix_right)):
            res.append(prefix_left[i - 1] * prefix_right[- i - 1])
        return res
        