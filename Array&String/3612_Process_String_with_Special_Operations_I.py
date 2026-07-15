class Solution(object):
    def processStr(self, s):
        """
        :type s: str
        :rtype: str

        time: O(2 ^ n), because '#', worst case all special characters are '#', will duplicate
        1, 2, 4, 8 ... times

        space: O(1) without considering output size, otherwise is O(2 ^ n) because '#'
        """
        
        ans = []

        for char in s:
            if char.isalpha():
                ans.append(char)
            elif ans and char == '*':
                ans.pop()
            elif char == '#':
                ans += ans
            elif char == '%':
                ans = ans[::-1]

        return ''.join(ans)
                