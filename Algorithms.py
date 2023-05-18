import math
class Algorithms():

    def linear_algoritm(self, x, y, z) -> float:
        return (5 * math.atan(x)) - ((1/4 * math.acos(x)) * ((x + 3 * abs(x - y) + x**2) / (abs(x - y) * z + x**2)))

    def f(self, func: str, x: float) -> float:
        if func == "cos(x)":
            return math.cos(x)
        elif func == "exp(x)":
            return math.exp(x)
        elif func == "sqr(x)":
            return x**2

    def ch(self, x):
        return (math.e**x + math.e**(-x)) / 2

    def branching_algorithm(self, x: float, y: float, func: str) -> float:
        if x * y < 5:
            return self.f(func, x)**3 + math.sin(y)
        elif x * y > 7:
            return self.ch(self.f(func, x)**3) + y**2
        else:
            return math.cos(x + self.f(func, x)**3)

if __name__ == "__main__":
    res = Algorithms()
    print(res.linear_algoritm(1, 2, 3))