class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        a, b = 0, len(s) - 1
        
        while a <= b:
            if s[a] != s[b]:
                return False
            a += 1
            b -= 1
        return True