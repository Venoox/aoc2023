import unittest
import solution


class TestDay8(unittest.TestCase):

    def test_sample(self):
        part1 = solution.part1("sample.txt")
        part2 = solution.part2("sample2.txt")
        self.assertEqual(part1, 6)
        self.assertEqual(part2, 6)

    def test_input(self):
        part1 = solution.part1("input.txt")
        part2 = solution.part2("input.txt")
        self.assertEqual(part1, 20569)
        self.assertEqual(part2, 21366921060721)


if __name__ == '__main__':
    unittest.main()
