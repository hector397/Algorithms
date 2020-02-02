import unittest
import insertion_sort


class TestInsertionSort(unittest.TestCase):

    def test__insertion_sort_increasing(self):
        """
        Test if the array is sorted correctly
        """

        array = [5, 2, 4, 6, 1, 3]
        array_sorted = [1, 2, 3, 4, 5, 6]

        insertion_sort.insertion_sort_increasing_order(array)

        self.assertListEqual(array, array_sorted, "Array is not sorted")

    def test__insertion_sort_decreasing(self):
        """
        Test if the array is sorted correctly
        """

        array = [5, 2, 4, 6, 1, 3]
        array_sorted = [6, 5, 4, 3, 2, 1]

        insertion_sort.insertion_sort_decreasing_order(array)

        self.assertListEqual(array, array_sorted, "Array is not sorted")

    def test__insertion_sort_empty_array(self):
        """
        Test if the array is sorted correctly
        """

        array = []
        array_sorted = []

        insertion_sort.insertion_sort_increasing_order(array)

        self.assertListEqual(array, array_sorted, "Array is not sorted")


if __name__ == '__main__':
    unittest.main()
