class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float

        nums1: [ left | right ]
        nums2: [ left | right ]

        goal is to make sure left == right to find median

        time: O(log(min(m,n)))
        space: O(1)
        """
        
        # find shorter nums 
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        # low means least number of element can take from nums1
        # high means most number can take from nums1
        # if [0, 1, 2] length is 3, but cut point we have is 4
        low, high = 0, m
        # if is odd length, m + n + 1 will make sure left have 1 more, median will located last of left part.
        half_len = (m + n + 1) // 2

        while low <= high:
            # find cut point for nums1
            i = (low + high) // 2
            # find cut point for nums2
            j = half_len - i

            if i > 0:
                l1 = nums1[i - 1]
            else:
                l1 = float('-inf')
            
            if i < m:
                r1 = nums1[i]
            else:
                r1 = float('inf')

            if j > 0:
                l2 = nums2[j - 1]
            else:
                l2 = float('-inf')

            if j < n:
                r2 = nums2[j]
            else:
                r2 = float('inf')

            # make sure: max(left part) <= min(right part)
            if l1 <= r2 and l2 <= r1:
                if(m + n) % 2 == 1:
                    return float(max(l1, l2))
                else:
                    # even num, we took max of L and min of max
                    return (max(l1, l2) + min(r1, r2)) / 2.0
                
            elif l1 > r2:
                # l1 too large, cut point of l1 need to move left
                high = i - 1
            else: # l2 > r1 l2 too large, cut point of l1 move to right
                low = i + 1

        

        