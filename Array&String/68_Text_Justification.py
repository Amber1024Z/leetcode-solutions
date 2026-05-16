class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        
        time: O(N) where N is the total number of characters in all words.
        space: O(N), we use lines to store the words for each line
        """
        lines = []

        # step 1, decide which words to put on each line
        i = 0
        while i < len(words):
            line_words = [words[i]]
            line_len = len(words[i])
            i += 1
            # remember + 1 for space after each word, check add next word, total length < maxWidth
            while i < len(words) and line_len + 1 + len(words[i]) <= maxWidth:
                line_len += 1 + len(words[i])
                line_words.append(words[i])
                i += 1

            lines.append(line_words)
        
        res = []
        # step 2, dealding space for each line
        for idx, line in enumerate(lines):
            # calculate curr line length
            word_len = 0
            for word in line:
                word_len += len(word)
            # calculate number of space at curr line
            space_num = maxWidth - word_len
            # gap num between word is number of word - 1, ex: 3 words need 2 gap
            gap_num = len(line) - 1
            
            # if it's last line OR this line contains 1 word, fill in the gaps with spaces
            if idx == len(lines) - 1 or gap_num == 0:
                res.append(' '.join(line) + ' ' * (maxWidth - gap_num - word_len))
            else:
                gap_width = space_num // gap_num
                # extra means how much extra space we have, also prev extra gap need +1
                extra = space_num % gap_num
                row = line[0]
                for j in range(gap_num):
                    if j < extra:
                        spaces = gap_width + 1
                    else:
                        spaces = gap_width
                    row += ' ' * spaces + line[j + 1]

                res.append(row)

        
        return res



