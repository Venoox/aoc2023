import unittest
import solution


class TestDay6(unittest.TestCase):

    def test_sample(self):
        part1 = solution.part1("sample.txt")
        part2 = solution.part2("sample.txt")
        self.assertEqual(part1, 288)
        self.assertEqual(part2, 71503)

    def test_input(self):
        part1 = solution.part1("input.txt")
        part2 = solution.part2("input.txt")
        self.assertEqual(part1, 771628)
        self.assertEqual(part2, 27363861)


if __name__ == '__main__':
    unittest.main()
