class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str

        if exsits x divides both str1 and str2, str1 = x + x + x ..., str2 = x + x + x ..., thus
        str1 + str2 == str2 + str1

        time: O(m + n)
        space: O(m + n), because we compare str1 + str2 == str2 + str1
        """

        if str1 + str2 != str2 + str1:
            return ''

        def get_gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        gcd_len = get_gcd(len(str1), len(str2))

        return str1[:gcd_len]
        
