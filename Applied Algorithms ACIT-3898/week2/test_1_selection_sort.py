from solution import selection_sort
from common_test_cases import AntiDiscoveryWrapper


class SelectionSortTest(AntiDiscoveryWrapper.CommonTestCase):
    def setUp(self):
        self._function_under_test = selection_sort