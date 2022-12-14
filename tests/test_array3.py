import unittest
import solutions.array3 as array3

class TestArray3(unittest.TestCase):
    def test_max_span(self):
        self.assertEqual(array3.max_span([1, 2, 1, 1, 3]), 4)
        self.assertEqual(array3.max_span([1, 4, 2, 1, 4, 1, 4]), 6)
        self.assertEqual(array3.max_span([1, 4, 2, 1, 4, 4, 4]), 6)
        self.assertEqual(array3.max_span([3, 3, 3]), 3)
        self.assertEqual(array3.max_span([3, 9, 3]), 3)
        self.assertEqual(array3.max_span([3, 9, 9]), 2)
        self.assertEqual(array3.max_span([3, 9]), 1)
        self.assertEqual(array3.max_span([3, 3]), 2)
        self.assertEqual(array3.max_span([]), 0)
        self.assertEqual(array3.max_span([1]), 1)
    
    def test_fix_34(self):
        self.assertEqual(array3.fix_34([1, 3, 1, 4]), [1, 3, 4, 1])
        self.assertEqual(array3.fix_34([1, 3, 1, 4, 4, 3, 1]), [1, 3, 4, 1, 1, 3, 4])
        self.assertEqual(array3.fix_34([3, 2, 2, 4]), [3, 4, 2, 2])
        self.assertEqual(array3.fix_34([3, 2, 3, 2, 4, 4]), [3, 4, 3, 4, 2, 2])
        self.assertEqual(array3.fix_34([2, 3, 2, 3, 2, 4, 4]), [2, 3, 4, 3, 4, 2, 2])
        self.assertEqual(array3.fix_34([5, 3, 5, 4, 5, 4, 5, 4, 3, 5, 3, 5]), [5, 3, 4, 5, 5, 5, 5, 5, 3, 4, 3, 4])
        self.assertEqual(array3.fix_34([3, 1, 4]), [3, 4, 1])
        self.assertEqual(array3.fix_34([3, 4, 1]), [3, 4, 1])
        self.assertEqual(array3.fix_34([1, 1, 1]), [1, 1, 1])
        self.assertEqual(array3.fix_34([1]), [1])
        self.assertEqual(array3.fix_34([]), [])
        self.assertEqual(array3.fix_34([7, 3, 7, 7, 4]), [7, 3, 4, 7, 7])
        self.assertEqual(array3.fix_34([3, 1, 4, 3, 1, 4]), [3, 4, 1, 3, 4, 1])
        self.assertEqual(array3.fix_34([3, 1, 1, 3, 4, 4]), [3, 4, 1, 3, 4, 1])
    
    def test_fix_45(self):
        self.assertEqual(array3.fix_45([5, 4, 9, 4, 9, 5]), [9, 4, 5, 4, 5, 9])
        self.assertEqual(array3.fix_45([1, 4, 1, 5]), [1, 4, 5, 1])
        self.assertEqual(array3.fix_45([1, 4, 1, 5, 5, 4, 1]), [1, 4, 5, 1, 1, 4, 5])
        self.assertEqual(array3.fix_45([4, 9, 4, 9, 5, 5, 4, 9, 5]), [4, 5, 4, 5, 9, 9, 4, 5, 9])
        self.assertEqual(array3.fix_45([5, 5, 4, 1, 4, 1]), [1, 1, 4, 5, 4, 5])
        self.assertEqual(array3.fix_45([4, 2, 2, 5]), [4, 5, 2, 2])
        self.assertEqual(array3.fix_45([4, 2, 4, 2, 5, 5]), [4, 5, 4, 5, 2, 2])
        self.assertEqual(array3.fix_45([4, 2, 4, 5, 5]), [4, 5, 4, 5, 2])
        self.assertEqual(array3.fix_45([1, 1, 1]), [1, 1, 1])
        self.assertEqual(array3.fix_45([4, 5]), [4, 5])
        self.assertEqual(array3.fix_45([5, 4, 1]), [1, 4, 5])
        self.assertEqual(array3.fix_45([]), [])
        self.assertEqual(array3.fix_45([5, 4, 5, 4, 1]), [1, 4, 5, 4, 5])
        self.assertEqual(array3.fix_45([4, 5, 4, 1, 5]), [4, 5, 4, 5, 1])
        self.assertEqual(array3.fix_45([3, 4, 5]), [3, 4, 5])
        self.assertEqual(array3.fix_45([4, 1, 5]), [4, 5, 1])
        self.assertEqual(array3.fix_45([5, 4, 1]), [1, 4, 5])
        self.assertEqual(array3.fix_45([2, 4, 2, 5]), [2, 4, 5, 2]	)
    
    def test_can_balance(self):
        self.assertEqual(array3.can_balance([1, 1, 1, 2, 1]), True)
        self.assertEqual(array3.can_balance([2, 1, 1, 2, 1]), False)
        self.assertEqual(array3.can_balance([10, 10]), True)
        self.assertEqual(array3.can_balance([10, 0, 1, -1, 10]), True)
        self.assertEqual(array3.can_balance([1, 1, 1, 1, 4]), True)
        self.assertEqual(array3.can_balance([2, 1, 1, 1, 4]), False)
        self.assertEqual(array3.can_balance([2, 3, 4, 1, 2]), False)
        self.assertEqual(array3.can_balance([1, 2, 3, 1, 0, 2, 3]), True)
        self.assertEqual(array3.can_balance([1, 2, 3, 1, 0, 1, 3]), False)
        self.assertEqual(array3.can_balance([1]), False)
        self.assertEqual(array3.can_balance([1, 1, 1, 2, 1]), True)
    
    def test_linear_in(self):
        self.assertEqual(array3.linear_in([1, 2, 4, 6], [2, 4]), True)
        self.assertEqual(array3.linear_in([1, 2, 4, 6], [2, 3, 4]), False)
        self.assertEqual(array3.linear_in([1, 2, 4, 4, 6], [2, 4]), True)
        self.assertEqual(array3.linear_in([2, 2, 4, 4, 6, 6], [2, 4]), True)
        self.assertEqual(array3.linear_in([2, 2, 2, 2, 2], [2, 2]), True)
        self.assertEqual(array3.linear_in([2, 2, 2, 2, 2], [2, 4]), False)
        self.assertEqual(array3.linear_in([2, 2, 2, 2, 4], [2, 4]), True)
        self.assertEqual(array3.linear_in([1, 2, 3], [2]), True)
        self.assertEqual(array3.linear_in([1, 2, 3], [-1]), False)
        self.assertEqual(array3.linear_in([1, 2, 3], []), True)
        self.assertEqual(array3.linear_in([-1, 0, 3, 3, 3, 10, 12], [-1, 0, 3, 12]), True)
        self.assertEqual(array3.linear_in([-1, 0, 3, 3, 3, 10, 12], [0, 3, 12, 14]), False)
        self.assertEqual(array3.linear_in([-1, 0, 3, 3, 3, 10, 12], [-1, 10, 11]), False)
    
    def test_sqaure_up(self):
        self.assertEqual(array3.square_up(3), [0, 0, 1, 0, 2, 1, 3, 2, 1])
        self.assertEqual(array3.square_up(2), [0, 1, 2, 1])
        self.assertEqual(array3.square_up(4), [0, 0, 0, 1, 0, 0, 2, 1, 0, 3, 2, 1, 4, 3, 2, 1])
        self.assertEqual(array3.square_up(1), [1])
        self.assertEqual(array3.square_up(0), [])
        self.assertEqual(array3.square_up(6), [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 1, 0, 0, 0, 3, 2, 1, 0, 0, 4, 3, 2, 1, 0, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1])
    
    def test_series_up(self):
        self.assertEqual(array3.series_up(3), [1, 1, 2, 1, 2, 3])
        self.assertEqual(array3.series_up(4), [1, 1, 2, 1, 2, 3, 1, 2, 3, 4])
        self.assertEqual(array3.series_up(2), [1, 1, 2])
        self.assertEqual(array3.series_up(1), [1])
        self.assertEqual(array3.series_up(0), [])
        self.assertEqual(array3.series_up(6), [1, 1, 2, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6])
    
    def test_max_mirror(self):
        self.assertEqual(array3.max_mirror([1, 2, 3, 8, 9, 3, 2, 1]), 3)
        self.assertEqual(array3.max_mirror([1, 2, 1, 4]), 3)
        self.assertEqual(array3.max_mirror([7, 1, 2, 9, 7, 2, 1]), 2)
        self.assertEqual(array3.max_mirror([21, 22, 9, 8, 7, 6, 23, 24, 6, 7, 8, 9, 25, 7, 8, 9]), 4)
        self.assertEqual(array3.max_mirror([1, 2, 1, 20, 21, 1, 2, 1, 2, 23, 24, 2, 1, 2, 1, 25]), 4)
        self.assertEqual(array3.max_mirror([1, 2, 3, 2, 1]), 5)
        self.assertEqual(array3.max_mirror([1, 2, 3, 3, 8]), 2)
        self.assertEqual(array3.max_mirror([1, 2, 7, 8, 1, 7, 2]), 2)
        self.assertEqual(array3.max_mirror([1, 1, 1]), 3)
        self.assertEqual(array3.max_mirror([1]), 1)
        self.assertEqual(array3.max_mirror([]), 0)
        self.assertEqual(array3.max_mirror([9, 1, 1, 4, 2, 1, 1, 1]), 3)
        self.assertEqual(array3.max_mirror([5, 9, 9, 4, 5, 4, 9, 9, 2]), 7)
        self.assertEqual(array3.max_mirror([5, 9, 9, 6, 5, 4, 9, 9, 2]), 2)
        self.assertEqual(array3.max_mirror([5, 9, 1, 6, 5, 4, 1, 9, 5]), 3)
    
    def test_count_clumps(self):
        self.assertEqual(array3.count_clumps([1, 2, 2, 3, 4, 4]), 2)
        self.assertEqual(array3.count_clumps([1, 1, 2, 1, 1]), 2)
        self.assertEqual(array3.count_clumps([1, 1, 1, 1, 1]), 1)
        self.assertEqual(array3.count_clumps([1, 2, 3]), 0)
        self.assertEqual(array3.count_clumps([2, 2, 1, 1, 1, 2, 1, 1, 2, 2]), 4)
        self.assertEqual(array3.count_clumps([0, 2, 2, 1, 1, 1, 2, 1, 1, 2, 2]), 4)
        self.assertEqual(array3.count_clumps([0, 0, 2, 2, 1, 1, 1, 2, 1, 1, 2, 2]), 5)
        self.assertEqual(array3.count_clumps([0, 0, 0, 2, 2, 1, 1, 1, 2, 1, 1, 2, 2]), 5)
        self.assertEqual(array3.count_clumps([]), 0)

if __name__ == '__main___':
    unittest.main()