class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.

        [0,0,0 | 1,1,1 | ? ? ? | 2,2,2]
              low     mid     high

        low, mid, high represents how many 0,1,2 we've already processed
        
        time: O(n)
        space: O(1)
        """

        low, mid, high = 0, 0, len(nums) - 1

        # mid point to curr num
        while mid <= high:
            # when nums is 0, swap mid and low
            # between low and mid must be 1, thus both pointers += 1
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            # when num is 2, swap mid and high
            else:
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1

        
        