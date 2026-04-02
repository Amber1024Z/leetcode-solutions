class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        time: n*(n-1)*(n-2)*⋯*1=n!, res.append(curr[:]) takes O(n), thus overall is n * n!
        space: O(n), The depth of the call stack is equal to the length of curr, which is limited to n.
        """
        res = []

        def backtrack(curr):
            if len(nums) == len(curr):
                res.append(curr[:])
                return

            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtrack(curr)
                    curr.pop()

        backtrack([])
        return res