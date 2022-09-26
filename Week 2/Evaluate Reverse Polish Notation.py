class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = "+-*"
        for i in range(len(tokens)):
            if tokens[i] == "/":
                result = eval(stack.pop() + "//" + stack.pop())
                stack.append(result)
            elif tokens[i] in ops:
                # DO CALC
                print (tokens[i])
                print(stack)
                exp = stack.pop()+ tokens[i] +stack.pop()
                result = eval(exp)
                stack.append(str(result))
            else:
                stack.append(tokens[i])
        return stack.pop()
