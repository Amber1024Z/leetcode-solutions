from collections import Counter
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool

        time: O(n)
        space: O(n)
        """

        counter = Counter(arr)

        return len(counter.values()) == len(set(counter.values()))
        