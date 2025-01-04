import Solution
import unittest


class TestSolution(unittest.TestCase):
    def test_evaluate(self):
        s = Solution.Solution()
        expression = "(let x 2 (mult x (let x 3 y 4 (add x y))))"
        self.assertEqual(s.evaluate(expression), 14)
        expression = "(let x 3 x 2 x)"
        self.assertEqual(s.evaluate(expression), 2)
        expression = "(let x 1 y 2 x (add x y) (add x y))"
        self.assertEqual(s.evaluate(expression), 5)




if __name__ == "__main__":
    unittest.main()
