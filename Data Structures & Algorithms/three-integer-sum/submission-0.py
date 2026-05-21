class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        i = 0
        while i < len(nums) - 2:
            if i > 0 and nums[i - 1] == nums[i]:
                i += 1
                continue
            
            left = i + 1
            right = len(nums) - 1

            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]
                if cur_sum > 0:
                    right -= 1
                elif cur_sum < 0:
                    left += 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1

                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

            i += 1

        return res
