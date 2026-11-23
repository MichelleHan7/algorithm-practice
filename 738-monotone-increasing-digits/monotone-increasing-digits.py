class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        strn = list(str(n))
        
        for i in range(len(strn)-2, -1, -1):
            if strn[i] > strn[i+1]:
                strn[i] = str(int(strn[i])-1)
                strn[i+1:] = '9' * (len(strn)-i-1)

        return int(''.join(strn))
