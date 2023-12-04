import unittest
import solution


class TestDay4(unittest.TestCase):

    def test_sample(self):
        part1, part2 = solution.solve("sample.txt")
        self.assertEqual(part1, 13)
        self.assertEqual(part2, 30)

    def test_input(self):
        part1, part2 = solution.solve("input.txt")
        self.assertEqual(part1, 21213)
        self.assertEqual(part2, 8549735)


if __name__ == '__main__':
    unittest.main()
