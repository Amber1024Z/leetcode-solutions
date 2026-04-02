class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        
        time: each letter corresponding 3-4 letters, 4^n, ''.join(cur) will take n times. Overall is n * (4^n)
        space: O(n), The maximum depth of the recursion is equal to the length n of the input string
        """
        if not digits: 
            return []

        map = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }

        result = []

        # i present current index, cur is current combination
        def make_combination(i, cur):
            # stop case, if hit the end, cur is not empty, add it to final result
            if i == len(digits):
                result.append(''.join(cur))
                return

            for char in map[digits[i]]:
                # make choice
                cur.append(char)
                #recursion 
                make_combination(i+1, cur)
                # Backtrack
                cur.pop()

        make_combination(0,[])

        return result