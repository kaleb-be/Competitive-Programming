class MyQueue:

    def __init__(self):
        self._stack = []
        

    def push(self, x: int) -> None:
        self._stack.append(x)

    def pop(self) -> int:
        temp =  self._stack[0]
        del self._stack[0]
        return temp
        

    def peek(self) -> int:
        return self._stack[0]
        

    def empty(self) -> bool:
        return self._stack==[]
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
