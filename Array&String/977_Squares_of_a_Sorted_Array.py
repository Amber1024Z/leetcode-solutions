class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        time: O(n)
        space: O(1) if don't consider output
        """
        
        n = len(nums)

        l, r = 0, n - 1

        res = [0] * n

        for i in range(n - 1, -1, -1):
            if abs(nums[l]) < abs(nums[r]):
                square = nums[r] * nums[r]
                res[i] = square
                r -= 1
            else:
                square = nums[l] * nums[l]
                res[i] = square
                l += 1

        return res
