class TrieNode:
    def __init__(self):
        self.children = {}
        # each node directly store 3 lexicographically minimums products.(alphabet order)
        self.suggestion = []

class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]

        time: M id number of product, apply sort will be MlogM * L, construct Trie, 
        L is average length of each product, will be M * L, S is length of search word.
        Thus total is O(MlogM * L + M*L + S)

        space: O(M * L)

        """
        products.sort()

        root = TrieNode()

        for product in products:
            node = root
            for char in product:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
                # ex: if first product is mobile, all 6 letters's suggestion will insert 'product'.
                if len(node.suggestion) < 3:
                    node.suggestion.append(product)
        
        res = []
        node = root
        # check in trie if is dead end
        is_end = False

        for char in searchWord:
            # if 1 char is not exsits in Trie, no need to check, just return [].
            if is_end or char not in node.children:
                is_end = True
                res.append([])
            else:
                node = node.children[char]
                res.append(node.suggestion)

        return res

        
        