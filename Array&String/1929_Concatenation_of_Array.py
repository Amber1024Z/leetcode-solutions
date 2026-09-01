class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        time: O(n)
        space: O(1)
        """
        
        n = len(nums)

        i = 0

        while i <= n - 1:
            curr = nums[i]
            nums.append(curr)

            i += 1

        return nums