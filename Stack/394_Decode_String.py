class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: strpp

        time: O(L),  every character that ultimately appears in the result has been pushed into the stack, popped from the stack and concatenated, the total time taken is linearly proportional to the length L of the final output.
        space: O(n), in worst case, we have all chars and numbers in stack, so space is O(n)

        """

        stack = []
        curr_num = 0
        curr_str = ''

        for char in s:
            """
            k * 10 + int(ch)
            ch='1': k = 0 * 10 + 1 = 1
            ch='2': k = 1 * 10 + 2 = 12
            ch='[': push k = 12 into count_stack 
            """
            if char.isdigit():
                curr_num = curr_num * 10 + int(char)
            elif char == '[':
                stack.append((curr_str, curr_num))
                curr_str = ''
                curr_num = 0
            elif char == ']':
                prev_str, prev_num = stack.pop()
                # string before '[' + curr_string * prev_num
                curr_str = prev_str + (curr_str * prev_num)
            else:
                curr_str += char

        return curr_str

        