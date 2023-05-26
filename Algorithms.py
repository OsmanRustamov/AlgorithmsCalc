import math
class Algorithms():

    def linear_algorithm(self, x: float, y: float, z: float) -> str:
        try:
            return str((5 * math.atan(x)) - ((1/4 * math.acos(x)) * ((x + 3 * abs(x - y) + x**2) / (abs(x - y) * z + x**2))))
        except:
            return "Введите переменные"
    def f(self, func: str, x: float) -> float:
        if func == "cos(x)":
            return math.cos(x)
        elif func == "exp(x)":
            return math.exp(x)
        elif func == "sqr(x)":
            return x**2

    def ch(self, x: float) -> float:
        return (math.e**x + math.e**(-x)) / 2

    def branching_algorithm(self, x: float, y: float, func: str) -> float | str:
        try:
            if x * y < 5:
                return self.f(func, x)**3 + math.sin(y)
            elif x * y > 7:
                return self.ch(self.f(func, x)**3) + y**2
            else:
                return math.cos(x + self.f(func, x)**3)
        except:
            return f"Введите переменные"
if __name__ == "__main__":
    res = Algorithms()
    print(res.linear_algoritm(1, 2, 3))