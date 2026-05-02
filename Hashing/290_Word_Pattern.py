class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool

        time: O(n), where n is the length of the pattern (or the number of words in s). We process each character in the pattern and each word in s exactly once.
        space: O(n), word can be different, we need to store them in dict, thus the space complexity is O(n).
        """

        map_char = {}
        map_word = {}

        words = s.split(' ')

        if len(pattern) != len(words):
            return False

        for s, word in zip(pattern, words):
            if (s not in map_char) and (word not in map_word):
                map_char[s] = word 
                map_word[word] = s 

            elif map_char.get(s) != word or map_word.get(word) != s:
                return False

        return True