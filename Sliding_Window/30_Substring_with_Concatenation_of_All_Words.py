from collections import Counter
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        
        time: O(n), outter loop iterate word_len times, each time iterate whole s, n / word_len times, overall is about O(n * word_len)
        space: O(n), w_counter is O(num_words * word_len), curr is also O(num_words * word_len), ans is O(n) in worst case.
        """

        word_len = len(words[0])
        need = len(words)
        w_counter = Counter(words)
        ans = []

        # when word_len = 3, start only able start from 0,3,6..or 1,4,7... or 2,5,8,...
        for offset in range(word_len):
            left = offset
            curr = Counter()
            have = 0

            # right is start idx for word, last word idx can't pass len(s) - word_len + 1
            for right in range(offset, len(s) - word_len + 1, word_len):
                word = s[right : right + word_len]
                
                # when word in counter, check window if it's valid first, then check if have == need
                if word in w_counter:
                    curr[word] += 1
                    have += 1

                    # when have > need, shrink from left
                    while curr[word] > w_counter[word]:
                        left_word = s[left: left + word_len]
                        curr[left_word] -= 1
                        have -= 1
                        left += word_len

                    # find target, shrink from left
                    if have == need:
                        ans.append(left)
                        # remove leftmost word
                        left_word = s[left: left + word_len]
                        curr[left_word] -= 1
                        have -= 1
                        left += word_len

                # if word does not match, reset window start idx to next word begins
                else:
                    curr.clear()
                    have = 0
                    left = right + word_len

        return ans