class Solution:
    def isHappy(self, n: int) -> bool:
        
        def getNext(n):
            res = 0
            while n:
                digit = n % 10
                res += digit ** 2
                n //= 10
            return res
        
        slow = n
        fast = getNext(n)
        
        while fast != 1 and slow != fast:
            slow = getNext(slow)
            fast = getNext(getNext(fast))
        
        return fast == 1