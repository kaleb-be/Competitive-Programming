class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        m = 0
        
        for i in range(0, len(A) - L - M + 1):
            sub1 = sum(A[i:i+L])
            for j in range(i + L, len(A) - M + 1):
                tot = sum(A[j:j+M]) + sub1
                if tot > m: 
                    m = tot
                    
        A.reverse()
        
        for i in range(0, len(A) - L - M + 1):
            sub1 = sum(A[i:i+L])
            for j in range(i + L, len(A) - M + 1):
                tot = sum(A[j:j+M]) + sub1
                if tot > m: 
                    m = tot           
        
        return m
