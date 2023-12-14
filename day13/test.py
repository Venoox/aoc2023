import unittest
import solution


class TestDay13(unittest.TestCase):

    def test_sample(self):
        part1 = solution.part1("sample.txt")
        part2 = solution.part2("sample.txt")
        self.assertEqual(part1, 405)
        self.assertEqual(part2, 400)

    def test_input(self):
        part1 = solution.part1("input.txt")
        part2 = solution.part2("input.txt")
        self.assertEqual(part1, 34772)
        self.assertEqual(part2, 35554)


if __name__ == '__main__':
    unittest.main()
