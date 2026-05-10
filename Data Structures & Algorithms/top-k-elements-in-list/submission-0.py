from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        arr =[[] for _ in range(len(nums) + 1)]

        for num, freq in cnt.items():
            arr[freq].append(num)

        res = []
        i = len(nums)
        while k > 0:
            j = 0
            while k > 0 and j < len(arr[i]):
                res.append(arr[i][j])
                j += 1
                k -= 1
            i -= 1
        return res



