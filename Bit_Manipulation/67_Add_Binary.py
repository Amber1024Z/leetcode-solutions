class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str

        time: O(max(N,M)), zfill create O(n) str, reverse/.join /for loop also takes O(n)
        space: O(max(N,M)), zfill create new str.

        space: 
        """
        n = max(len(a), len(b))
        # zfill, fill string with 0 until length == n
        # "101".zfill(5) -> "00101"
        a, b = a.zfill(n), b.zfill(n)

        carry = 0
        ans = []

        for i in range(n - 1, -1, -1):
            colSum = carry

            # 当前位的和 = a[i] + b[i] + carry，这个和只可能是 0、1、2、3。
            if a[i] == '1':
                colSum += 1
            if b[i] == '1':
                colSum += 1

            # if colSum == 1 or  == 3, curr col should be 1
            if colSum%  2 == 1:
                ans.append('1')
            else:
                ans.append('0')

            # 0 or 1 carry 都是0，只有2，3才会有1个carry
            if colSum == 2 or colSum == 3:
                carry = 1
            else:
                carry = 0
        
        if carry == 1:
            ans.append('1')

        ans.reverse()

        return ''.join(ans)

        