class TrieNode:
    def __init__(self):
        self.children = {}
        # word to store curr word for result
        self.word = None

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        
        time:  M * 4 * 3^(L-1), M is number of cells in board, L is the maximum length of words. First step we have 4 direction 
        to search, after that we have at most 3 direction to search because we can't go back to the cell we just come from. We do 
        this for L-1 times because we already search the first letter in the first step.
        
        space: O(N) where N is the total number of letters in the words list, word number * average length of word. Size for the trie.
        """
        root = TrieNode()

        # like prev questions: insert
        # constrcut trie for words
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word

        rowNum, colNum = len(board), len(board[0])
        res = []

        def backtrack(row, col, parent):
            letter = board[row][col]
            currNode = parent.children[letter]

            # if we find match word
            if currNode.word:
                res.append(currNode.word)
                # avoid duplicate
                currNode.word = None

            board[row][col] = '#'

            for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                new_r, new_c = row + dr, col + dc

                if new_r < 0 or new_r >=rowNum or new_c < 0 or new_c >= colNum:
                    continue
                if board[new_r][new_c] not in currNode.children:
                    continue

                backtrack(new_r, new_c, currNode)

            # after searching, restore to prev letter
            board[row][col] = letter

            # remove empty leaf node, pruning, ex: eat, t don't have children, we can delete
            if not currNode.children:
                del parent.children[letter]
        
        for row in range(rowNum):
            for col in range(colNum):
                if board[row][col] in root.children:
                    backtrack(row, col, root)

        return res


        