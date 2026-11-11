class Logger:

    def __init__(self):
        self.grace_period = defaultdict(int)

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.grace_period:
            self.grace_period[message] = timestamp + 10
            return True
        else:
            if self.grace_period[message] <= timestamp:
                self.grace_period[message] = timestamp + 10
                return True
            else:
                return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)