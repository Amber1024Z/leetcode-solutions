class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.

        time: O(n)
        space: O(1)
        """

        # point to last non-zero idx from nums1
        p1 = m - 1
        # point to last idx from nums2
        p2 = n - 1
        # point to last idx from nums1
        p = m + n - 1

        # scan from right to left, find largest element from num1 and nums2, put on end of nums1
        for i in range(p, -1, -1):
            # compare all element from nums2 with num1, since nums1 it's already sorted
            if p2 < 0:
                break
            elif p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[i] = nums1[p1]
                p1 -= 1
            else:
                nums1[i] = nums2[p2]
                p2 -= 1




