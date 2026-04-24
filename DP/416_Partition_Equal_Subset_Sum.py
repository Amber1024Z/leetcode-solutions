class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        time: O(n * target), where n is the length of the input array and target is the total sum divided by 2
        space: O(target)
        """
        total = sum(nums)

        # if the total sum is odd, we cannot partition it into two equal subsets
        if total % 2 == 1:
            return False

        target = total // 2
        
        # dp[i] means whether we can sum up to i using the numbers in the array
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            # we will stop when i == num, because we cannot sum up to a number less than num using num
            for i in range(target, num - 1, -1):
                if dp[i - num] == True:
                    dp[i] = True

            # early stop if we have already found a subset that sums up to target, because remaining numbers must sum up to target as well
            if dp[target]:
                return True

        return dp[target]
        