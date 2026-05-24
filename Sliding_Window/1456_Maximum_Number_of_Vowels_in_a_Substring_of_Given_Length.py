class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int

        time: O(n)
        sapce: O(1), vowels is constant space
        """
        
        vowels = {'a', 'e', 'i', 'o', 'u'}
        count = 0
        for char in s[:k]:
            if char in vowels:
                count  += 1

        ans = count
        
        for i in range(k, len(s)):
            # check curr s[i] if it's vowel
            if s[i] in vowels:
                count += 1
            # check leftmost if it's vowel
            if s[i - k] in vowels:
                count -= 1
            ans = max(count, ans)

        return ans
                

