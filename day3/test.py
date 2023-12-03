import unittest
import solution


class TestDay3(unittest.TestCase):

    def test_sample(self):
        part1, part2 = solution.solve("sample.txt")
        self.assertEqual(part1, 4361)
        self.assertEqual(part2, 467835)

    def test_input(self):
        part1, part2 = solution.solve("input.txt")
        self.assertEqual(part1, 533784)
        self.assertEqual(part2, 78826761)


if __name__ == '__main__':
    unittest.main()
