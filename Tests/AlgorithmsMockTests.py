import sys
import unittest
from unittest import mock
from Algorithms import Algorithms


class MyTestCase(unittest.TestCase):
    Algorithms = Algorithms()

    def test_linear(self):
        with mock.patch.object(self.Algorithms, 'linear_algorithm', return_value=3.9269908169872414) as mock_linear:
            self.assertEqual(self.Algorithms.linear_algorithm(1, 2, 3), 3.9269908169872414)
            mock_linear.assert_called_once_with(1, 2, 3)

    def test_linear_1(self):
        with mock.patch.object(self.Algorithms, 'linear_algorithm', return_value="Введите переменные") as mock_linear:
            self.assertEqual(self.Algorithms.linear_algorithm(1, 2, ""), "Введите переменные")
            mock_linear.assert_called_once_with(1, 2, "")

    def test_branch_1(self):
        with mock.patch.object(self.Algorithms, 'branching_algorithm', return_value=1.0670260320766751) as mock_branch:
            self.assertEqual(self.Algorithms.branching_algorithm(1, 2, "cos(x)"), 1.0670260320766751)
            mock_branch.assert_called_once_with(1, 2, "cos(x)")

    def test_branch_2(self):
        with mock.patch.object(self.Algorithms, 'branching_algorithm', return_value=1.9092974268256817) as mock_branch:
            self.assertEqual(self.Algorithms.branching_algorithm(1, 2, "exp(x)"), 1.9092974268256817)
            mock_branch.assert_called_once_with(1, 2, "exp(x)")

    def test_branch_3(self):
        with mock.patch.object(self.Algorithms, 'branching_algorithm', return_value=20.994834350013345) as mock_branch:
            self.assertEqual(self.Algorithms.branching_algorithm(1, 2, "sqr(x)"), 20.994834350013345)
            mock_branch.assert_called_once_with(1, 2, "sqr(x)")

    def test_branch_4(self):
        with mock.patch.object(self.Algorithms, 'branching_algorithm', return_value="Введите переменные") as mock_branch:
            self.assertEqual(self.Algorithms.branching_algorithm(1, 2, ""), "Введите переменные")
            mock_branch.assert_called_once_with(1, 2, "")


if __name__ == '__main__':
    unittest.main()