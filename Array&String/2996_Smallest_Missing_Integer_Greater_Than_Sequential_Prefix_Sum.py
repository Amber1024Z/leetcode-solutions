class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        time: O(n)
        space: O(1)
        """
        
        # longest sequential prefix MUST start with nums[0]
        prefix_sum = nums[0]

        # find sum of ongest sequential prefix
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                prefix_sum += nums[i]
            else:
                break

        # check will reduce to O(1)
        seen = set(nums)

        x = prefix_sum
        
        while x in seen:
            x += 1

        return x
            