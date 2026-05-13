class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        
        time: O(n), each element is pushed and popped at most once, so overall time is O(n)
        space: O(n), in worst case, we have decreasing temperatures, so all idx will be in stack, so space is O(n)
        """
        n = len(temperatures)
        ans = [0] * n
        # stack to store idx, temperatures in stack is decresing
        stack = []

        for i in range(n):
            # if curr temperature is higher than temperatures in stack, pop prev temp and calculate days
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_idx = stack[-1]
                ans[prev_idx] = i - prev_idx
                # pop out prev idx
                stack.pop()
            
            stack.append(i)

        return ans
