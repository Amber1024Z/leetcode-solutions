class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        
        time: O(n + m) where n is the length of haystack and m is the length of needle. We are building LPS array in O(m) and then searching in O(n).
        space: O(m) for LPS array.
        """
        m = len(needle)
        n = len(haystack)

        if n < m:
            return -1

        # build LPS(ongest Proper Prefix which is also Suffix) for needle
        lps = [0] * m
        # current position of the prefix
        prev = 0
        # lps[0] always be 0 since it's single str
        i = 1

        while i < m:
            if needle[i] == needle[prev]:
                # lps will increase
                prev += 1
                lps[i] = prev
                i += 1
            else:
                if prev == 0:
                    lps[i] = 0
                    i += 1
                # Try finding longest border for this i with reduced prev
                else:
                    prev = lps[prev - 1]

        h_ptr = 0
        n_ptr = 0

        while h_ptr < n:
            if haystack[h_ptr] == needle[n_ptr]:
                h_ptr += 1
                n_ptr += 1

                if n_ptr == m:
                    # m characters behind last matching will be window start
                    return h_ptr - m
            else:
                # if nothing macthed also n_ptr == 0, only move h_ptr
                if n_ptr == 0:
                    h_ptr += 1
                # shift left n_ptr
                else:
                    n_ptr = lps[n_ptr - 1]

        return -1






                    


                    