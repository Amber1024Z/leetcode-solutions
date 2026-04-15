from collections import defaultdict

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        spcae/time: O(n)
        """
        count = curr_sum = 0

        # store prefix sum value
        h = defaultdict(int)

        for num in nums:
            curr_sum += num

            if curr_sum == k:
                count += 1

            # curr_sum - k = prefix, if prefix already in dict, means curr_sum - prefix = k, count += 1
            # thus count should equal how many times prefix exits
            count += h[curr_sum -  k]

            h[curr_sum] += 1

        return count