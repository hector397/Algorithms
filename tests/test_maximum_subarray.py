import unittest
import maximum_subarray


class TestMaximumSubarray(unittest.TestCase):

    def test__brute_force_maximum_subarray(self):
        """
        Test if the subarray is correct using the brute-force method
        """

        array = [4, -5, 1, 2, 8, -2, 4, 6, 0, 7, -1]
        left, right, sum = 2, 9, 26

        result_left, result_right, result_sum = maximum_subarray.brute_force_maximum_subarray(array, 0, len(array))

        self.assertEqual(left, result_left, "Left bound incorrect")
        self.assertEqual(right, result_right, "Right bound incorrect")
        self.assertEqual(sum, result_sum, "Sum incorrect")

    def test_brute_force_maximum_subarray_size_1(self):
        """
        Test if the subarray is correct using the brute-force method when the array size is 1
        """

        array = [4]
        left, right, sum = 0, 0, 4

        result_left, result_right, result_sum = maximum_subarray.brute_force_maximum_subarray(array, 0, 0)

        self.assertEqual(left, result_left, "Left bound incorrect")
        self.assertEqual(right, result_right, "Right bound incorrect")
        self.assertEqual(sum, result_sum, "Sum incorrect")

    def test_brute_force_maximum_subarray_empty(self):
        """
        Test if the subarray is correct usin the brute-force method when the array is empty
        """

        array = []
        left, right, sum = 0, 0, 0

        result_left, result_right, result_sum = maximum_subarray.brute_force_maximum_subarray(array, 0, len(array))

        self.assertEqual(left, result_left, "Left bound incorrect")
        self.assertEqual(right, result_right, "Right bound incorrect")
        self.assertEqual(sum, result_sum, "Sum incorrect")

    def test_maximum_crossing_subarray(self):
        """
        Test if the maximum crossing subarray is correct
        """
        array = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
        left, right, sum = 7, 10, 43

        result_left, result_right, result_sum = maximum_subarray.find_max_crossing_subarray(array, 0, 7, 15)

        self.assertEqual(left, result_left, "Left bound incorrect")
        self.assertEqual(right, result_right, "Right bound incorrect")
        self.assertEqual(sum, result_sum, "Sum incorrect")

    def test_recursive_maximum_subarray(self):
        """
        Test if the maximum subarray using recursivity is correct
        """

        array = [4, -5, 1, 2, 8, -2, 4, 6, 0, 7, -1]
        left, right, sum = 2, 9, 26

        result_left, result_right, result_sum = maximum_subarray.recursive_maximum_subarray(array, 0, len(array) - 1)

        self.assertEqual(left, result_left, "Left bound incorrect")
        self.assertEqual(right, result_right, "Right bound incorrect")
        self.assertEqual(sum, result_sum, "Sum incorrect")

    def test_recursive_maximum_subarray_size_1(self):
        """
        Test if the subarray is correct using the recursive method when the array size is 1
        """

        array = [4]
        left, right, sum = 0, 0, 4

        result_left, result_right, result_sum = maximum_subarray.recursive_maximum_subarray(array, 0, 0)

        self.assertEqual(left, result_left, "Left bound incorrect")
        self.assertEqual(right, result_right, "Right bound incorrect")
        self.assertEqual(sum, result_sum, "Sum incorrect")

    def test_recursive_maximum_subarray_empty(self):
        """
        Test if the subarray is correct usin the recursive method when the array is empty
        """

        array = []
        left, right, sum = 0, 0, 0

        result_left, result_right, result_sum = maximum_subarray.recursive_maximum_subarray(array, 0, len(array))

        self.assertEqual(left, result_left, "Left bound incorrect")
        self.assertEqual(right, result_right, "Right bound incorrect")
        self.assertEqual(sum, result_sum, "Sum incorrect")


if __name__ == '__main__':
    unittest.main()
