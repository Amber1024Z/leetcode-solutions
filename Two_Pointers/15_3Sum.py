class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        
        time: O(n^2) because we have two nested loops. The outer loop runs n times and the inner loop runs n times in the worst case.
        space: O(logn) because of timsort's space complexity. 
        """
        
        result = []
        # from low to high
        nums.sort()

        for i in range(len(nums)):
            # check duplicate, skip
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j, k = i + 1, len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    
                    # skip duplicate j
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    # skip duplicate k
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1

                    j += 1
                    k -= 1
                    
                elif total < 0:
                    j += 1
                else:
                    k -= 1

        return result
