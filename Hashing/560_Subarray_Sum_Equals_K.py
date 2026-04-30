from collections import defaultdict
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        time: O(n)
        space: O(n), worse case, we have n different prefix sum, and we need to store them in dict.
        """
        count = curr_sum = 0

        # store prefix sum value
        h = defaultdict(int)

        for num in nums:
            curr_sum += num

            if curr_sum == k:
                count += 1

            # consider curr_sum is 10, k is 2, prefix[8] is 3, from prefix[8] to curr_sum 10, we have 3 subarray sum equals k
            count += h[curr_sum -  k]

            # store curr_sum prefix sum value into dict, if curr_sum already exists, we add 1 to the value, otherwise we create a new key with value 1
            h[curr_sum] += 1

        return count



