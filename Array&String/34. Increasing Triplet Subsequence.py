class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        time: O(n)
        space: O(1)
        """
        first = float('inf')
        second = float('inf')

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            # if num bigger than first and second, return True
            else:
                return True
        
        return False

        