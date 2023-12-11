import unittest
import solution


class TestDay11(unittest.TestCase):

    def test_sample(self):
        part1 = solution.part1("sample.txt")
        part2 = solution.part2("sample.txt")
        self.assertEqual(part1, 374)
        self.assertEqual(part2, 82000210)

    def test_input(self):
        part1 = solution.part1("input.txt")
        part2 = solution.part2("input.txt")
        self.assertEqual(part1, 9418609)
        self.assertEqual(part2, 593821230983)


if __name__ == '__main__':
    unittest.main()
