import unittest


class AntiDiscoveryWrapper:
    class CommonTestCase(unittest.TestCase):
        def setUp(self):
            # subclasses had better set this to a sorting function
            self._function_under_test = None

        def __do_test(self, before):
            expected = sorted(before)
            actual = before[:]
            self._function_under_test(actual)
            self.assertListEqual(expected, actual)

        def test_empty(self):
            self.__do_test([])

        def test_single_0(self):
            self.__do_test([0])

        def test_single_2(self):
            self.__do_test([2])

        def test_single_negative(self):
            self.__do_test([-22])

        def test_single_large(self):
            self.__do_test([1e8])

        def test_1_2(self):
            self.__do_test([1, 2])

        def test_2_1(self):
            self.__do_test([2, 1])

        def test_4_1_3_2(self):
            self.__do_test([4, 1, 3, 2])

        def test_4_3_1_2(self):
            self.__do_test([4, 3, 1, 2])

        def test_1_2_3_4(self):
            self.__do_test([1, 2, 3, 4])

        def test_1_3_2_4(self):
            self.__do_test([1, 3, 2, 4])

        def test_negatives_desc(self):
            self.__do_test([-1, -2, -3, -4])

        def test_negatives_asc(self):
            self.__do_test([-4, -3, -2, -1])

        def test_negatives_positives(self):
            self.__do_test([5, -5, 10, -10, 15, -15])