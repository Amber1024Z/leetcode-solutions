class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool

        time: O(n), We process each character in both the strings exactly once to determine if the strings are isomorphic.
        space: O(1) since the size of the ASCII character set is fixed
        """
        
        mapping_s_t = {}
        mapping_t_s = {}

        for c1, c2 in zip(s, t):
            if (c1 not in mapping_s_t) and (c2 not in mapping_t_s):
                mapping_s_t[c1] = c2
                mapping_t_s[c2] = c1

            elif mapping_s_t.get(c1) != c2 or mapping_t_s.get(c2) != c1:
                return False

        return True




        