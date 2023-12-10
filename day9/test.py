import unittest
import solution


class TestDay9(unittest.TestCase):

    def test_sample(self):
        part1 = solution.part1("sample.txt")
        part2 = solution.part2("sample.txt")
        self.assertEqual(part1, 114)
        self.assertEqual(part2, 2)

    def test_input(self):
        part1 = solution.part1("input.txt")
        part2 = solution.part2("input.txt")
        self.assertEqual(part1, 1708206096)
        self.assertEqual(part2, 1050)


if __name__ == '__main__':
    unittest.main()
