from collections import defaultdict
import collections
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]

        time complexity: O(n * klogk),where n is the length of strs, and k is the maximum length of a string in strs. 
        The outer loop has complexity O(N) as we iterate through each string. Then, we sort each string in O(KlogK) time.

        Space Complexity: O(NK), the total information content stored in ans.
        """
        # defaultdict accessing a key that has not yet been stored will automatically create an empty list
        ans = collections.defaultdict(list)

        for s in strs:
            # sorted string a -> z
            char_list = sorted(s)

            # convert it into tuple as KEY
            # ex: ate -> ('a', 'e', 't')
            key = tuple(char_list)

            ans[key].append(s)

        return list(ans.values())

        

