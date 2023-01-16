class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        x = 1
        lst = [1]
        while 3 ** x < (2 ** 31) - 1:
            lst.append(3**x)
            x+=1
        return n in lst
        
