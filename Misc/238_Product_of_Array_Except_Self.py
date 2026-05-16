class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        nums =  [1, 2, 3, 4]
        prefix= [1, 1, 2, 6]   # prefix[i] = i left product
        suffix= [24,12,4, 1]   # suffix[i] = i right product
        ans=    [24,12,8, 6]   # ans[i] = prefix[i] * suffix[i]

        time: O(n)
        space: O(1)
        """

        # calculate prefix first
        ans = [1] * len(nums)

        # first prefix always be 1, since nothing on left
        # remember * nums[i - 1] since we calculate product on i's left not include i
        for i in range(1, len(nums)):
            ans[i] = ans[i - 1] * nums[i - 1]
        
        # there's nothing on right, so first suffix from right also be 1
        suffix = 1

        for j in range(len(nums) - 1, -1, -1):
            ans[j] = ans[j] * suffix
            # update suffix from right to left
            suffix = suffix * nums[j]

        return ans


