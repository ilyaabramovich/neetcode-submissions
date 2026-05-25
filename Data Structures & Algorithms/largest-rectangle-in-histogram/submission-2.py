class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []
        for index, height in enumerate(heights):
            start = index
            while stack and  height < stack[-1][1]:
                i, h = stack.pop()
                res = max(res, (index - i) * h) 
                start = i
            stack.append((start, height))


        for i, h in stack:
            res = max(res, h * (len(heights) - i))
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

        