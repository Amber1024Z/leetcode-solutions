class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.

        time: O(n)
        space: O(1)
        """

        def reverse_nums(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        n = len(nums)
        k = k % n

        # reverse whole array, ex: [1, 2, 3, 4, 5, 6, 7] -> [7, 6, 5, 4, 3, 2, 1]
        reverse_nums(nums, 0, n - 1)
        # reverse num before k, ex: [7, 6, 5, 4, 3, 2, 1] -> [5, 6, 7, 4, 3, 2, 1]
        reverse_nums(nums, 0, k - 1)
        # reverse num after k, ex: [5, 6, 7, 4, 3, 2, 1] -> [5, 6, 7, 1, 2, 3, 4]
        reverse_nums(nums, k, n - 1)