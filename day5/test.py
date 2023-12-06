import unittest
import solution


class TestDay5(unittest.TestCase):

    def test_sample(self):
        part1 = solution.part1("sample.txt")
        part2 = solution.part2("sample.txt")
        self.assertEqual(part1, 35)
        self.assertEqual(part2, 46)

    def test_input(self):
        part1 = solution.part1("input.txt")
        part2 = solution.part2("input.txt")
        self.assertEqual(part1, 227653707)
        self.assertEqual(part2, 78775051)


if __name__ == '__main__':
    unittest.main()
