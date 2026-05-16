class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        XOR:
        1. a ^ 0 = a
        2. a ^ a = 0
        3. a ^ b ^ a = b

        time: O(n)
        space: O(1)
        """

        a = 0

        for num in nums:
            a ^= num

        return a 

        