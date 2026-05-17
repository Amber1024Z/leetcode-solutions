class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int

        When a smaller number appears to the left of a larger number, use subtraction
        ex: IX, I is on left of X, so 10 - 1 = 9

        I(1): before V(5) and X(10) 
        X(5): before L(50) and C(100)
        C(100): before D(500) and M(1000)
        
        time: O(1) because 1 <= s.length <= 15
        space: O(1) because size of values is fixed = 7
        """
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        
        # Typically accumulated from left to right
        # smaller number precedes the larger number, subtract the smaller number

        # we can update from tail to head
        total  = values[s[-1]]

        # Start checking from the second-to-last one
        for i in range(len(s) - 2, -1, -1)  :
            # If the current value is less than the value on the right, subtract it; otherwise, add it.
            if values[s[i]] < values[s[i + 1]]:
                total -= values[s[i]]
            else:
                total += values[s[i]]

        return total