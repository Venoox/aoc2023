import unittest
import solution


class TestDay16(unittest.TestCase):

    def test_sample(self):
        part1 = solution.part1("sample.txt")
        part2 = solution.part2("sample.txt")
        self.assertEqual(part1, 46)
        self.assertEqual(part2, 51)

    def test_input(self):
        part1 = solution.part1("input.txt")
        part2 = solution.part2("input.txt")
        self.assertEqual(part1, 7788)
        self.assertEqual(part2, 7987)


if __name__ == '__main__':
    unittest.main()
