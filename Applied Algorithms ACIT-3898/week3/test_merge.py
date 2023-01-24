from mergesort import merge
import random
import unittest


class MergeTest(unittest.TestCase):
    def helper(self, left, right, _):
        expected = sorted(left + right)
        actual = merge(left, right)
        self.assertListEqual(
            expected,
            actual,
            f"merged {left} and {right}, expected {expected}, but got {actual}",
        )

    def setUp(self):
        pass

    def test_12_34(self):
        self.helper([1, 2], [3, 4], [1, 2, 3, 4])

    def test_34_12(self):
        self.helper([3, 4], [1, 2], [1, 2, 3, 4])

    def test_1_234(self):
        self.helper([1], [2, 3, 4], [1, 2, 3, 4])

    def test_3_124(self):
        self.helper([3], [1, 2, 4], [1, 2, 3, 4])

    def test_empty_left(self):
        self.helper([], [1, 3, 5], [1, 3, 5])

    def test_empty_right(self):
        self.helper([1, 3, 5], [], [1, 3, 5])

    def many_random_tests(self, num, size):
        for i in range(num):
            seed = 10001 * i
            random.seed(seed)
            left = []
            right = []
            for _ in range(size):
                if random.random() < 0.5:
                    left.append(random.randint(1, size * 10))
                else:
                    right.append(random.randint(1, size * 10))
            left.sort()
            right.sort()
            self.helper(left, right, None)

    def test_100_random_len100(self):
        self.many_random_tests(100, 100)

    def test_200_random_len50(self):
        self.many_random_tests(200, 50)

    def test_20_random_len300(self):
        self.many_random_tests(20, 300)