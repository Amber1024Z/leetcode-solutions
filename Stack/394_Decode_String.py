class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: strpp
        
        time: O(n * k_max), k_max is the max number to repeat, but we can consider k_max as a constant, so overall time is O(n)
        space: O(n), in worst case, we have all chars and numbers in stack, so space is O(n)
        """

        count_stack = []
        string_stack = []
        curr_str = ''
        k = 0

        for char in s:
            """
            k * 10 + int(ch)
            ch='1': k = 0 * 10 + 1 = 1
            ch='2': k = 1 * 10 + 2 = 12
            ch='[': push k = 12 into count_stack 
            """
            if char.isdigit():
                k = k * 10 + int(char)
            elif char == '[':
                count_stack.append(k)
                # right now curr_str is str before '['
                string_stack.append(curr_str)
                curr_str = ''
                k = 0
            elif char == ']':
                prev_str = string_stack.pop()
                # string before '[' + curr_string * k
                curr_str = prev_str + (curr_str * count_stack.pop())
            else:
                curr_str += char

        return curr_str

        