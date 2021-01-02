class Solution:
    def convert(self, s: str, numRows: int) -> str:
        r = ["" for _ in range(numRows)]
        cyc = numRows*2-2
        if cyc == 0:
            return s
        for i in range(numRows):
            for j in range(len(s)):
                mod = j%cyc
                if mod >= numRows:
                    idx = mod - numRows
                    mod = numRows - idx - 2
                # equal
                if mod == i:
                    r[i] = r + s[j]
        return r
