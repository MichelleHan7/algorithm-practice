class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        sign = 1
        ans = 0
        i = 0
        
        # ignore all whitespaces
        while i < n and s[i] == ' ':
            i += 1

        # determine the sign
        if i < n and s[i] in '+-':
            if s[i] == '-':
                sign = -1
            i += 1
        
        while i < n and '0' <= s[i] <= '9':
            digit = ord(s[i]) - ord('0')
            ans = ans * 10 + digit
            i += 1
        
        ans *= sign
        return max(-2 ** 31, min(ans, 2 ** 31 - 1))
        