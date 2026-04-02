class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
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
                if len(cur) > 0:
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