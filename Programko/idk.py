class ahoj():
    def __init__(self, a):
        self.a = a
        self.do()

    def do(self):
        return self.a[::-1]

print(ahoj("ahoj"))