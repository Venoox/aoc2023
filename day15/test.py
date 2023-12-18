import unittest
import solution


class TestDay15(unittest.TestCase):

    def test_sample(self):
        part1 = solution.part1("sample.txt")
        part2 = solution.part2("sample.txt")
        self.assertEqual(part1, 1320)
        self.assertEqual(part2, 145)

    def test_input(self):
        part1 = solution.part1("input.txt")
        part2 = solution.part2("input.txt")
        self.assertEqual(part1, 497373)
        self.assertEqual(part2, 259356)


if __name__ == '__main__':
    unittest.main()
