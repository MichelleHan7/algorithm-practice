class MyQueue:

    def __init__(self):
        self.st_in = []
        self.st_out = []

    def push(self, x: int) -> None:
        self.st_in.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        if self.st_out:
            return self.st_out.pop()
        else:
            for i in range(len(self.st_in)):
                val = self.st_in.pop()
                self.st_out.append(val)
            return self.st_out.pop()

    def peek(self) -> int:
        if self.empty():
            return None
        if self.st_out:
            return self.st_out[-1]
        else:
            for i in range(len(self.st_in)):
                val = self.st_in.pop()
                self.st_out.append(val)
            return self.st_out[-1]

    def empty(self) -> bool:
        return len(self.st_in) == 0 and len(self.st_out) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()