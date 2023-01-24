from solution import bubble_sort
from common_test_cases import AntiDiscoveryWrapper


class BubbleSortTest(AntiDiscoveryWrapper.CommonTestCase):
    def setUp(self):
        self._function_under_test = bubble_sort