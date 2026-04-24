class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        time: O(n log n) we traverse the array once (O(n)) and for each element, we perform a binary search 
        on the sub array (O(log n))
        space: O(n) we use a sub array to store the longest increasing subsequence, in the worst case, the 
        longest increasing subsequence can be the entire array, so the space complexity is O(n)
        """

        if not nums:
            return 0 

        if len(nums) == 1:
            return 1

        # we have 2 options for each number in the array: 
        # 1: either we can append it to the longest increasing subsequence if it is greater than the last number in the sub array
        # 2: or we can replace the first number in the sub array that is greater than or equal to the current number with the current number
        sub = []

        for num in nums:
            # if the sub array is empty or the current number is greater than the last number in the sub array, we can append the current number to the sub array
            if not sub or num > sub[-1]:
                sub.append(num)
            # find first insert pos >= num 
            else:
                l, r = 0, len(sub) - 1

                while l < r:
                    m = (l + r) // 2
                    if sub[m] < num:
                        l = m + 1
                    # sub[m] >= num
                    else:
                        r = m
                # stop when l == r, l is the first insert pos >= num, we replace the number at that position with the current number
                sub[l] = num
        
        return len(sub)


