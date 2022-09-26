class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        pairs = {'(' : ')', '[' : ']', '{' : '}'}
        stack = []
        for i in s:
            if i in pairs.keys():
                stack.append(i)
            else:
                if stack == []:
                    return False
                a = stack.pop()
                if i!= pairs[a]:
                    return False
        return stack == []
