class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        # always add to the regular stack
        self.stack.append(val)

        # For the min, if min stack is empty, just add it
        # if new val is smaller, add new val
        # if new val is larger, readd the current min

        if not self.mins or val < self.mins[-1]:
            self.mins.append(val)
        else:
            self.mins.append(self.mins[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]