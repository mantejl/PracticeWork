class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = [homepage]
        self.forwardHist = []

    def visit(self, url: str) -> None:
        self.current.append(url)
        self.forwardHist.clear()

    def back(self, steps: int) -> str:
        size = min(steps, len(self.current) - 1)
        for _ in range(0, size):
            self.forwardHist.append(self.current.pop())
        return self.current[-1]

    def forward(self, steps: int) -> str:
        size = min(steps, len(self.forwardHist))
        for _ in range(0, size):
            self.current.append(self.forwardHist.pop())
        return self.current[-1]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)