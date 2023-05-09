import unittest
from teste import MathSamples


class FibonacciTest(unittest.TestCase):

    def test_fib01(self):
        """Testanco caso pra entrada 5"""
        self.assertEqual(
            MathSamples.fibonacci(6),
            8
        )