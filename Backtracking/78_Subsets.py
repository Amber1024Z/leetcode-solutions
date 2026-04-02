class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        
        time: n number will have 2^n subsets, ex:[1, 2. 3] has 8, res.append(curr[:]) take n times, overall is n * (2^n)
        space: O(n)
        """
        res = []
        n = len(nums)

        def backtrack(curr, start):
            # each node is a subset, we can add it to res, since it's list, we need shallow copy
            res.append(curr[:])

            for i in range(start, n):
                curr.append(nums[i])
                backtrack(curr, i + 1)
                curr.pop()

        backtrack([], 0)
        return res
        