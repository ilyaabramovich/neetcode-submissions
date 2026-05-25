class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        for i in range(len(heights)):
            cur = heights[i]
            k = 1
            for j in range(i + 1, len(heights)):
                res = max(res, cur * k)
                if heights[i] == 0:
                    break
                cur = min(cur, heights[j])
                k += 1
            res = max(res, cur * k)

        return res
            




        # stack = [[heights[0], 1]]
        # res = 0

        # for i in range(1, len(heights)):
        #     height = heights[i]
        #     if height > stack[-1][0]:
        #         res = max(res, stack[-1][0] * (stack[-1][1] + 1))
        #         stack[-1][1] += 1
        #     else:
        #         res = max(res, stack[-1][0] * stack[-1][1])
        #         temp = [min(stack[-1][0], height), stack[-1][1] + 1]
        #         if temp[0] * temp[1] > res:
        #             stack[-1] = temp
        # print(stack)
        # return res

        