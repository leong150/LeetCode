class Solution:
    def convert(self, s: str, numRows: int) -> str:
      ans = ''
      if numRows == 1:
        ans = s
      else:
        for i in range(numRows):
          for j in range(i, len(s), 2 * (numRows - 1)):
            ans += s[j]
            if i != 0 and i != numRows - 1:
              if j + 2 * (numRows - 1 - i) < len(s):
                ans += s[j + 2 * (numRows - 1 - i)]
      return ans

Zigzag_conversion = Solution()
print(Zigzag_conversion.convert(s = 'PAYPALISHIRING', numRows = 4))
