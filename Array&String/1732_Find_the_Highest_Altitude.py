class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int

        time: O(n)
        space: O(1)
        """
        curr = max_g = 0

        for g in gain:
            curr += g
            max_g = max(max_g, curr)

        return max_g