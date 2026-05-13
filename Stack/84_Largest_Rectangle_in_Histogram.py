class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int

        For each column, the maximum width of the rectangle it can form depends on the positions of the first columns to its left and right that are shorter than it
        
        time: O(n), each height will calculate area once, and each height is pushed and popped at most once, so overall time is O(n)
        space: O(n), in worst case, we have increasing heights, so all idx will be in stack, so space is O(n)

        """
        ans = 0
        # increasing stack, store idx for height
        # store -1 to deal edge case, curr height < than prev height, if pop out, stack will be empty, if visit stack[-1] will be problem
        stack = [-1]
        n = len(heights)

        for i in range(n):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                curr_height = heights[stack.pop()]
                # i is first right height < curr height, stack[-1] is first left height < curr_hright
                curr_width = i - stack[-1] -1
                ans = max(ans, curr_height * curr_width)
            # push idx to stack to calulate width
            stack.append(i)

        # iterate remain height in stack, they maintain increasing order
        while stack[-1] != -1:
            curr_height = heights[stack.pop()]
            curr_width = len(heights) - stack[-1] -1
            ans = max(ans, curr_height * curr_width)

        return ans


