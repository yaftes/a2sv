class Node:
    def __init__(self,url):
        self.url = url
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        val = Node(homepage)
        self.current = val
    

    def visit(self, url: str) -> None:
        # add current url and make the next of it none
        # make current the new one
        newpage = Node(url)
        self.current.next = newpage
        newpage.prev = self.current
        self.current = newpage
        return

    def back(self, steps: int) -> str:
        temp = self.current
        while temp.prev and steps > 0:
            temp = temp.prev
            steps -= 1
        self.current = temp
        return self.current.url
        

    def forward(self, steps: int) -> str:
        temp = self.current
        while temp.next and steps > 0:
            temp = temp.next
            steps -= 1
        self.current = temp
        return self.current.url
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)