import unittest
import solution


class TestDay7(unittest.TestCase):

    def test_sample(self):
        part1 = solution.part1("sample.txt")
        part2 = solution.part2("sample.txt")
        self.assertEqual(part1, 6440)
        self.assertEqual(part2, 5905)

    def test_input(self):
        part1 = solution.part1("input.txt")
        part2 = solution.part2("input.txt")
        self.assertEqual(part1, 253933213)
        self.assertEqual(part2, 253473930)


if __name__ == '__main__':
    unittest.main()
