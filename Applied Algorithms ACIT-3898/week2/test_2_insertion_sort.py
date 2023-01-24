from solution import insertion_sort
from common_test_cases import AntiDiscoveryWrapper


class InsertionSortTest(AntiDiscoveryWrapper.CommonTestCase):
    def setUp(self):
        self._function_under_test = insertion_sort