from collections import Counter
class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int

        time: O(n)
        space: O(1)

        time: O(M + N)
        space: O(1), text only contains lower case, 26 letters.
        """
        pattern = 'balloon'

        counter1 = Counter(pattern)
        counter2 = Counter(text)

        ans = float('inf')

        for char in pattern:
            ans = min(ans, counter2[char] // counter1[char])

        return ans