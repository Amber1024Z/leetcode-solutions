class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        when count = 0, choose curr num as candidate, if meet diff num, count -= 1
        candidate at end must be majority num since more then n // 2

        time: O(n)
        space: O(1)
        """
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate
        