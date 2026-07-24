class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        time: O(nlog(s)), s is search range and s = sum(nums)- max(nums). for each s will takes
        O(n) because get_group will iterate all num in nums

        space: O(1)
        """
        
        low, high = max(nums), sum(nums)

        # try with largets sum, if we can fit with k groups
        def get_group(largest_sum):
            group = 1
            curr_sum = 0

            for num in nums:
                if curr_sum + num > largest_sum:
                    group += 1
                    curr_sum = num
                else:
                    curr_sum += num

            return group

        ans = float('inf')

        while low <= high:
            m = (low + high) // 2

            if get_group(m) <= k:
                high = m - 1
                ans = min(ans, m)
            else:
                low = m + 1

        return ans