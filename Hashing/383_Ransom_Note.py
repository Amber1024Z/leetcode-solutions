from collections import defaultdict

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool

        time: O(m + n), where m is the length of magazine and n is the length of ransomNote.
        space: O(1), we only need to store 26 lowercase letters in dict, so the space complexity is O(1).
        """
        counter = defaultdict(int)

        for char in magazine:
            counter[char] += 1

        for char in ransomNote:
            if counter[char] <= 0:
                return False
            
            counter[char] -= 1

        return True