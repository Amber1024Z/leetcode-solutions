class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool

        time: O(n)
        space: O(K), we use a sliding window to store the numbers in the range of k
        """

        seen = set()
        # we use a sliding window to store the numbers in the range of k, if we find a duplicate number in the sliding window, 
        # return true, otherwise we add the number to the sliding window, if the size of sliding window is greater than k, we 
        # remove the leftmost number in the sliding window.
        for i, num in enumerate(nums):
            if num in seen:
                return True
            seen.add(num)
            if len(seen) > k:
                seen.remove(nums[i - k]) 
        return False