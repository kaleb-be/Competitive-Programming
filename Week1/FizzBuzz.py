class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        if n>=10**4:
            return
        answer=[]
        for i in range(1,n+1):
            if i % 3 == 0:
                if i % 5 == 0:
                    answer.append("FizzBuzz")
                else:
                    answer.append("Fizz")
            elif i % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(f"{i}")
        return answer
