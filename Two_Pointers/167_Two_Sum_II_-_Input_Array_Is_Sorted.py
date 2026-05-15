class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]

        time: O(n)
        space: O(1)
        """

        l, r = 0, len(numbers) - 1

        # we keep narrow down the range, since it's ordered
        while l < r:
            curr_sum = numbers[l] + numbers[r]

            if curr_sum == target:
                # since index strat from 1 not 0, we +1
                return [l + 1, r + 1]
            elif curr_sum < target:
                l += 1
            else:
                r -= 1

        return []

