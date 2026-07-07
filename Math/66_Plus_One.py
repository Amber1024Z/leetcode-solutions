
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]

        time: O(n) since it's not more than one pass along the input list.
        
        space: O(n), n the worst scenario, we would need to allocate an intermediate space to hold the result, which contains the N+1 elements. Ex: [9, 9, 9] will
        result in [1, 0, 0, 0] 

        """
        # check from right to left
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] != 9:
                digits[i] = digits[i] + 1
                return digits
            # if digit is 0, change to 0
            else:
                digits[i] = 0

        # when we walk here, means all digit are 9, should inset at first pos
        return [1] + digits
