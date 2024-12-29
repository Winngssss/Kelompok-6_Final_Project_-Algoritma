class Euclid:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def gcd(self):
        a, b = self.a, self.b
        while b:
            a, b = b, a % b
        return a