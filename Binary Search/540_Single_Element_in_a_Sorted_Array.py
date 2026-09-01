class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        time: O(logn) for binary search
        space: O(1)
        """
        
        # for valid pair, idx will looks like (even, odd), ex: (0, 1), (2, 3), (4, 5)... thus we use binary
        # search to find singile number which break the rule

        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2

            # we trying to make m locate on even idx, which is start of pair
            if m % 2 == 1:
                m -= 1

            # if curr pair is valid, signle must locate on right half
            if nums[m] == nums[m + 1]:
                l = m + 2
            # if it's not, signle number must on left
            else:
                r = m

        return nums[l]