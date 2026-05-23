class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int

        time: O(n)
        space: O(1)
        """
        # i represents curr visit idx, j represents 'written' idx
        i, j = 0, 0

        while i < (len(chars)):
            curr = chars[i]
            count = 0

            while i < len(chars) and chars[i] == curr:
                count += 1
                i += 1

            # meet diff char, in-place modify
            chars[j] = curr
            j += 1

            # convert count to str
            if count > 1:
                for digit in str(count):
                    chars[j] = digit
                    j += 1
        
        return j


        