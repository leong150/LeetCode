class Solution:
    def longestPalindrome(self, s: str) -> str:
        for i in range(len(s),1,-1):
            for j in range(0,len(s)-i):
                substring = s[j:j+i]
                if substring[::-1] == substring:
                    return substring

palindrome = Solution()
print(palindrome.longestPalindrome(s="1fd5g41bb14gs351"))