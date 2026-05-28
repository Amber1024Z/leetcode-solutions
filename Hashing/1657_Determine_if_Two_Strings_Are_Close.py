from collections import Counter
class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool

        time: O(m + n)
        space: O(1), since we only have 26 lowercase English letters
        """
        if len(word1) != len(word2):
            return False

        counter1 = Counter(word1)
        counter2 = Counter(word2)

        # make sure str from word1 and word2 are same
        if set(counter1.keys()) != set(counter2.keys()):
            return False
        
        # if frequency also equal, means we can swap word2 to word1
        return sorted(counter1.values()) == sorted(counter2.values())