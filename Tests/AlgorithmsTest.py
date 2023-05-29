import unittest
from Algorithms import Algorithms


class MyTestCase(unittest.TestCase):
    def test_linear_algoritm(self):
        self.assertEqual(Algorithms().linear_algorithm(1, 2, 3), 3.9269908169872414)

    def test_linear_algoritm_1(self):
        self.assertEqual(Algorithms().linear_algorithm(1, 2, 3), 3.9269908169872414)

    def test_linear_algoritm_2(self):
        self.assertEqual(Algorithms().linear_algorithm(1, 2, ""), "Введите переменные")

    def test_branching_algoritm(self):
        self.assertEqual(Algorithms().branching_algorithm(1, 2, "cos(x)"), 1.0670260320766751)

    def test_branching_algoritm_1(self):
        self.assertEqual(Algorithms().branching_algorithm(1, 2, "sqr(x)"), 1.9092974268256817)

    def test_branching_algoritm_2(self):
        self.assertEqual(Algorithms().branching_algorithm(1, 2, "exp(x)"), 20.994834350013345)

    def test_branching_algoritm_3(self):
        self.assertEqual(Algorithms().branching_algorithm(1, "", "exp(x)"), "Введите переменные")


if __name__ == '__main__':
    unittest.main()
