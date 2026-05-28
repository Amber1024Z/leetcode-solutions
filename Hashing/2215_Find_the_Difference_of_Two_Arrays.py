class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]

        time: O(m + n)
        space: O(m + n)
        """

        set1 = set(nums1)
        set2 = set(nums2)

        # will automatically find unique number in num1 and nums2
        return [list(set1 - set2), list(set2 - set1)]