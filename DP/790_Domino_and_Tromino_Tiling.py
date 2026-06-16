class Solution(object):
    def numTilings(self, n):
        """
        :type n: int
        :rtype: int

        f(k) = f(k - 1) + f(k - 2) + 2 * p(k - 1)
        
        time: O(n)
        space: O(n)
        """

        MOD = 10 ** 9 + 7

        if n <= 2:
            return n

        # fully covered board
        f = [0] * (n + 1)

        # partially cover board, p[k] represent k - 1 cols are fully covered, on k col upper right is empty. 
        p = [0] * (n + 1)

        f[1] = 1
        f[2] = 2
        p[2] = 1
        
        """
        f[k - 1]: The board of width k - 1 is fully covered. We transition to f[k] by placing 1 vertical domino at the very end.
        f[k - 2]: The board of width k - 2 is fully covered. We transition to f[k] by placing 2 horizontal dominoes (one on top of the other) to fill the remaining 2*2 space.
        p[k - 1] From the 1st to the k - 2 column are fully covered, and the k - 1 column has 1 square uncovered (e.g., upper-right). We transition to f[k] by placing 1 L-shaped tromino to fill the gap and the rest of the k-th column. Since upper-right and lower-right gaps are perfectly symmetrical, we multiply by 2 to account for both.
        """
        for k in range(3, n + 1):
            f[k] = (f[k - 1] + f[k - 2] + 2 * p[k - 1]) % MOD
            # p[k - 1]: k - 2 cols are fully covered, on k - 1 uppper right and k col is empty
            # p[k - 1]: place a domino on upper row, on k col will left a space on upper right corner
            # f[k - 2]: place a L-shape, on k col will left a space on upper right corner
            p[k] = (p[k -1] + f[k - 2]) % MOD

        return f[n]