import unittest
import source.array2 as array2

class TestArray2(unittest.TestCase):
    def test_count_evens(self):
        self.assertEqual(array2.count_evens([2, 1, 2, 3, 4]), 3)
        self.assertEqual(array2.count_evens([2, 2, 0]), 3)
        self.assertEqual(array2.count_evens([1, 3, 5]), 0)
        self.assertEqual(array2.count_evens([]), 0)
        self.assertEqual(array2.count_evens([11, 9, 0, 1]), 1)
        self.assertEqual(array2.count_evens([2, 11, 9, 0]), 2)
        self.assertEqual(array2.count_evens([2]), 1)
        self.assertEqual(array2.count_evens([2, 5, 12]), 2)
    
    def test_big_diff(self):
        self.assertEqual(array2.big_diff([10, 3, 5, 6]), 7)
        self.assertEqual(array2.big_diff([7, 2, 10, 9]), 8)
        self.assertEqual(array2.big_diff([2, 10, 7, 2]), 8)
        self.assertEqual(array2.big_diff([2, 10]), 8)
        self.assertEqual(array2.big_diff([10, 2]), 8)
        self.assertEqual(array2.big_diff([10, 0]), 10)
        self.assertEqual(array2.big_diff([2, 3]), 1)
        self.assertEqual(array2.big_diff([2, 2]), 0)
        self.assertEqual(array2.big_diff([2]), 0)
        self.assertEqual(array2.big_diff([5, 1, 6, 1, 9, 9]), 8)
        self.assertEqual(array2.big_diff([7, 6, 8, 5]), 3)
        self.assertEqual(array2.big_diff([7, 7, 6, 8, 5, 5, 6]), 3)

    def test_centered_average(self):
        self.assertEqual(array2.centered_average([1, 2, 3, 4, 100]), 3)
        self.assertEqual(array2.centered_average([1, 1, 5, 5, 10, 8, 7]), 5)
        self.assertEqual(array2.centered_average([-10, -4, -2, -4, -2, 0]), -3)
        self.assertEqual(array2.centered_average([5, 3, 4, 6, 2]), 4)
        self.assertEqual(array2.centered_average([5, 3, 4, 0, 100]), 4)
        self.assertEqual(array2.centered_average([100, 0, 5, 3, 4]), 4)
        self.assertEqual(array2.centered_average([4, 0, 100]), 4)
        self.assertEqual(array2.centered_average([0, 2, 3, 4, 100]), 3)
        self.assertEqual(array2.centered_average([1, 1, 100]), 1)
        self.assertEqual(array2.centered_average([7, 7, 7]), 7)
        self.assertEqual(array2.centered_average([1, 7, 8]), 7)
        self.assertEqual(array2.centered_average([1, 1, 99, 99]), 50)
        self.assertEqual(array2.centered_average([1000, 0, 1, 99]), 50)
        self.assertEqual(array2.centered_average([4, 4, 4, 4, 5]), 4)
        self.assertEqual(array2.centered_average([4, 4, 4, 1, 5]), 4)
        self.assertEqual(array2.centered_average([6, 4, 8, 12, 3]), 6)
    
    def test_sum_13(self):
        self.assertEqual(array2.sum_13([1, 2, 2, 1]), 6)
        self.assertEqual(array2.sum_13([1, 1]), 2)
        self.assertEqual(array2.sum_13([1, 2, 2, 1, 13]), 6)
        self.assertEqual(array2.sum_13([1, 2, 13, 2, 1, 13]), 4)
        self.assertEqual(array2.sum_13([13, 1, 2, 13, 2, 1, 13]), 3)
        self.assertEqual(array2.sum_13([]), 0)
        self.assertEqual(array2.sum_13([13]), 0)
        self.assertEqual(array2.sum_13([13, 13]), 0)
        self.assertEqual(array2.sum_13([13, 0, 13]), 0)
        self.assertEqual(array2.sum_13([13, 1, 13]), 0)
        self.assertEqual(array2.sum_13([5, 7, 2]), 14)
        self.assertEqual(array2.sum_13([5, 13, 2]), 5)
        self.assertEqual(array2.sum_13([0]), 0)
        self.assertEqual(array2.sum_13([13, 0]), 0)
    
    def test_sum_67(self):
        self.assertEqual(array2.sum_67([1, 2, 2]), 5)
        self.assertEqual(array2.sum_67([1, 2, 2, 6, 99, 99, 7]), 5)
        self.assertEqual(array2.sum_67([1, 1, 6, 7, 2]), 4)
        self.assertEqual(array2.sum_67([1, 6, 2, 2, 7, 1, 6, 99, 99, 7]), 2)
        self.assertEqual(array2.sum_67([1, 6, 2, 6, 2, 7, 1, 6, 99, 99, 7]), 2)
        self.assertEqual(array2.sum_67([2, 7, 6, 2, 6, 7, 2, 7]), 18)
        self.assertEqual(array2.sum_67([2, 7, 6, 2, 6, 2, 7]), 9)
        self.assertEqual(array2.sum_67([1, 6, 7, 7]), 8)
        self.assertEqual(array2.sum_67([6, 7, 1, 6, 7, 7]), 8)
        self.assertEqual(array2.sum_67([6, 8, 1, 6, 7]), 0)
        self.assertEqual(array2.sum_67([]), 0)
        self.assertEqual(array2.sum_67([6, 7, 11]), 11)
        self.assertEqual(array2.sum_67([11, 6, 7, 11]), 22)
        self.assertEqual(array2.sum_67([2, 2, 6, 7, 7]), 11)
    
    def test_has_22(self):
        self.assertEqual(array2.has_22([1, 2, 2]), True)
        self.assertEqual(array2.has_22([1, 2, 1, 2]), False)
        self.assertEqual(array2.has_22([2, 1, 2]), False)
        self.assertEqual(array2.has_22([2, 2, 1, 2]), True)
        self.assertEqual(array2.has_22([1, 3, 2]), False)
        self.assertEqual(array2.has_22([1, 3, 2, 2]), True)
        self.assertEqual(array2.has_22([2, 3, 2, 2]), True)
        self.assertEqual(array2.has_22([4, 2, 4, 2, 2, 5]), True)
        self.assertEqual(array2.has_22([1, 2]), False)
        self.assertEqual(array2.has_22([2, 2]), True)
        self.assertEqual(array2.has_22([2]), False)
        self.assertEqual(array2.has_22([]), False)
        self.assertEqual(array2.has_22([3, 3, 2, 2]), True)
        self.assertEqual(array2.has_22([5, 2, 5, 2]), False)
    
    def test_luckey_13(self):
        self.assertEqual(array2.lucky_13([0, 2, 4]), True)
        self.assertEqual(array2.lucky_13([1, 2, 3]), False)
        self.assertEqual(array2.lucky_13([1, 2, 4]), False)
        self.assertEqual(array2.lucky_13([2, 7, 2, 8]), True)
        self.assertEqual(array2.lucky_13([2, 7, 1, 8]), False)
        self.assertEqual(array2.lucky_13([3, 7, 2, 8]), False)
        self.assertEqual(array2.lucky_13([2, 7, 2, 1]), False)
        self.assertEqual(array2.lucky_13([1, 2]), False)
        self.assertEqual(array2.lucky_13([2, 2]), True)
        self.assertEqual(array2.lucky_13([2]), True)
        self.assertEqual(array2.lucky_13([3]), False)
        self.assertEqual(array2.lucky_13([]), True)
    
    def test_sum_28(self):
        self.assertEqual(array2.sum_28([2, 3, 2, 2, 4, 2]), True)
        self.assertEqual(array2.sum_28([2, 3, 2, 2, 4, 2, 2]), False)
        self.assertEqual(array2.sum_28([1, 2, 3, 4]), False)
        self.assertEqual(array2.sum_28([2, 2, 2, 2]), True)
        self.assertEqual(array2.sum_28([1, 2, 2, 2, 2, 4]), True)
        self.assertEqual(array2.sum_28([]), False)
        self.assertEqual(array2.sum_28([2]), False)
        self.assertEqual(array2.sum_28([8]), False)
        self.assertEqual(array2.sum_28([2, 2, 2]), False)
        self.assertEqual(array2.sum_28([2, 2, 2, 2, 2]), False)
        self.assertEqual(array2.sum_28([1, 2, 2, 1, 2, 2]), True)
        self.assertEqual(array2.sum_28([5, 2, 2, 2, 4, 2]), True)

    def test_more_14(self):
        self.assertEqual(array2.more_14([1, 4, 1]), True)
        self.assertEqual(array2.more_14([1, 4, 1, 4]), False)
        self.assertEqual(array2.more_14([1, 1]), True)
        self.assertEqual(array2.more_14([1, 6, 6]), True)
        self.assertEqual(array2.more_14([1]), True)
        self.assertEqual(array2.more_14([1, 4]), False)
        self.assertEqual(array2.more_14([6, 1, 1]), True)
        self.assertEqual(array2.more_14([1, 6, 4]), False)
        self.assertEqual(array2.more_14([1, 1, 4, 4, 1]), True)
        self.assertEqual(array2.more_14([1, 1, 6, 4, 4, 1]), True)
        self.assertEqual(array2.more_14([]), False)
        self.assertEqual(array2.more_14([4, 1, 4, 6]), False)
        self.assertEqual(array2.more_14([4, 1, 4, 6, 1]), False)
        self.assertEqual(array2.more_14([1, 4, 1, 4, 1, 6]), True)
    
    def test_fizz_array(self):
        self.assertEqual(array2.fizz_array(4), [0, 1, 2, 3])
        self.assertEqual(array2.fizz_array(1), [0])
        self.assertEqual(array2.fizz_array(10), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] )
        self.assertEqual(array2.fizz_array(0), [])
        self.assertEqual(array2.fizz_array(2), [0, 1])
        self.assertEqual(array2.fizz_array(7), [0, 1, 2, 3, 4, 5, 6])
    
    def test_only_14(self):
        self.assertEqual(array2.only_14([1, 4, 1, 4]), True)
        self.assertEqual(array2.only_14([1, 4, 2, 4]), False)
        self.assertEqual(array2.only_14([1, 1]), True)
        self.assertEqual(array2.only_14([4, 1]), True)
        self.assertEqual(array2.only_14([2]), False)
        self.assertEqual(array2.only_14([]), True)
        self.assertEqual(array2.only_14([1, 4, 1, 3]), False)
        self.assertEqual(array2.only_14([3, 1, 3]), False)
        self.assertEqual(array2.only_14([1]), True)
        self.assertEqual(array2.only_14([4]), True)
        self.assertEqual(array2.only_14([3, 4]), False)
        self.assertEqual(array2.only_14([1, 3, 4]), False)
        self.assertEqual(array2.only_14([1, 1, 1]), True)
        self.assertEqual(array2.only_14([1, 1, 1, 5]), False)
        self.assertEqual(array2.only_14([4, 1, 4, 1]), True)
    
    def test_fizz_array_2(self):
        self.assertEqual(array2.fizz_array_2(4),  ['0', '1', '2', '3'])
        self.assertEqual(array2.fizz_array_2(10), ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
        self.assertEqual(array2.fizz_array_2(2), ['0', '1'])
        self.assertEqual(array2.fizz_array_2(1), ['0'])
        self.assertEqual(array2.fizz_array_2(0), [])
        self.assertEqual(array2.fizz_array_2(7), ['0', '1', '2', '3', '4', '5', '6'])
        self.assertEqual(array2.fizz_array_2(9), ['0', '1', '2', '3', '4', '5', '6', '7', '8'])
        self.assertEqual(array2.fizz_array_2(11), ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
    
    def test_no_14(self):
        self.assertEqual(array2.no_14([1, 2, 3]), True)
        self.assertEqual(array2.no_14([1, 2, 3, 4]), False)
        self.assertEqual(array2.no_14([2, 3, 4]), True)
        self.assertEqual(array2.no_14([1, 1, 4, 4]), False)
        self.assertEqual(array2.no_14([2, 2, 4, 4]), True)
        self.assertEqual(array2.no_14([2, 3, 4, 1]), False)
        self.assertEqual(array2.no_14([2, 1, 1]), True)
        self.assertEqual(array2.no_14([1, 4]), False)
        self.assertEqual(array2.no_14([2]), True)
        self.assertEqual(array2.no_14([2, 1]), True)
        self.assertEqual(array2.no_14([1]), True)
        self.assertEqual(array2.no_14([4]), True)
        self.assertEqual(array2.no_14([]), True)
        self.assertEqual(array2.no_14([1, 1, 1, 1]), True)
        self.assertEqual(array2.no_14([9, 4, 4, 1]), False)
        self.assertEqual(array2.no_14([4, 2, 3, 1]), False)
        self.assertEqual(array2.no_14([4, 2, 3, 5]), True)
        self.assertEqual(array2.no_14([4, 4, 2]), True)
        self.assertEqual(array2.no_14([1, 4, 4]), False)
    
    def test_is_everywhere(self):
        self.assertEqual(array2.is_everywhere([1, 2, 1, 3], 1), True)
        self.assertEqual(array2.is_everywhere([1, 2, 1, 3], 2), False)
        self.assertEqual(array2.is_everywhere([1, 2, 1, 3, 4], 1), False)
        self.assertEqual(array2.is_everywhere([2, 1, 2, 1], 1), True)
        self.assertEqual(array2.is_everywhere([2, 1, 2, 1], 2), True)
        self.assertEqual(array2.is_everywhere([2, 1, 2, 3, 1], 2), False)
        self.assertEqual(array2.is_everywhere([3, 1], 3), True)
        self.assertEqual(array2.is_everywhere([3, 1], 2), False)
        self.assertEqual(array2.is_everywhere([3], 1), True)
        self.assertEqual(array2.is_everywhere([], 1), True)
        self.assertEqual(array2.is_everywhere([1, 2, 1, 2, 3, 2, 5], 2), True)
        self.assertEqual(array2.is_everywhere([1, 2, 1, 1, 1, 2], 2), False)
        self.assertEqual(array2.is_everywhere([2, 1, 2, 1, 1, 2], 2), False)
        self.assertEqual(array2.is_everywhere([2, 1, 2, 2, 2, 1, 1, 2], 2), False)
        self.assertEqual(array2.is_everywhere([2, 1, 2, 2, 2, 1, 2, 1], 2), True)
        self.assertEqual(array2.is_everywhere([2, 1, 2, 1, 2], 2), True)
    
    def test_either_24(self):
        self.assertEqual(array2.either_24([1, 2, 2]), True)
        self.assertEqual(array2.either_24([4, 4, 1]), True)
        self.assertEqual(array2.either_24([4, 4, 1, 2, 2]), False)
        self.assertEqual(array2.either_24([1, 2, 3, 4]), False)
        self.assertEqual(array2.either_24([3, 5, 9]), False)
        self.assertEqual(array2.either_24([1, 2, 3, 4, 4]), True)
        self.assertEqual(array2.either_24([2, 2, 3, 4]), True)
        self.assertEqual(array2.either_24([1, 2, 3, 2, 2, 4]), True)
        self.assertEqual(array2.either_24([1, 2, 3, 2, 2, 4, 4]), False)
        self.assertEqual(array2.either_24([1, 2]), False)
        self.assertEqual(array2.either_24([2, 2]), True)
        self.assertEqual(array2.either_24([4, 4]), True)
        self.assertEqual(array2.either_24([2]), False)
        self.assertEqual(array2.either_24([]), False)
    
    def test_match_up(self):
        self.assertEqual(array2.match_up([1, 2, 3], [2, 3, 10]), 2)
        self.assertEqual(array2.match_up([1, 2, 3], [2, 3, 5]), 3)
        self.assertEqual(array2.match_up([1, 2, 3], [2, 3, 3]), 2)
        self.assertEqual(array2.match_up([5, 3], [5, 5]), 1)
        self.assertEqual(array2.match_up([5, 3], [4, 4]), 2)
        self.assertEqual(array2.match_up([5, 3], [3, 3]), 1)
        self.assertEqual(array2.match_up([5, 3], [2, 2]), 1)
        self.assertEqual(array2.match_up([5, 3], [1, 1]), 1)
        self.assertEqual(array2.match_up([5, 3], [0, 0]), 0)
        self.assertEqual(array2.match_up([4], [4]), 0)
        self.assertEqual(array2.match_up([4], [5]), 1)

    def test_has_77(self):
        self.assertEqual(array2.has_77([1, 7, 7]), True)
        self.assertEqual(array2.has_77([1, 7, 1, 7]), True)
        self.assertEqual(array2.has_77([1, 7, 1, 1, 7]), False)
        self.assertEqual(array2.has_77([7, 7, 1, 1, 7]), True)
        self.assertEqual(array2.has_77([2, 7, 2, 2, 7, 2]), False)
        self.assertEqual(array2.has_77([2, 7, 2, 2, 7, 7]), True)
        self.assertEqual(array2.has_77([7, 2, 7, 2, 2, 7]), True)
        self.assertEqual(array2.has_77([7, 2, 6, 2, 2, 7]), False)
        self.assertEqual(array2.has_77([7, 7, 7]), True)
        self.assertEqual(array2.has_77([7, 1, 7]), True)
        self.assertEqual(array2.has_77([7, 1, 1]), False)
        self.assertEqual(array2.has_77([1, 2]), False)
        self.assertEqual(array2.has_77([1, 7]), False)
        self.assertEqual(array2.has_77([7]), False)
    
    def test_has_12(self):
        self.assertEqual(array2.has_12([1, 3, 2]), True)
        self.assertEqual(array2.has_12([3, 1, 2]), True)
        self.assertEqual(array2.has_12([3, 1, 4, 5, 2]), True)
        self.assertEqual(array2.has_12([3, 1, 4, 5, 6]), False)
        self.assertEqual(array2.has_12([3, 1, 4, 1, 6, 2]), True)
        self.assertEqual(array2.has_12([2, 1, 4, 1, 6, 2]), True)
        self.assertEqual(array2.has_12([2, 1, 4, 1, 6]), False)
        self.assertEqual(array2.has_12([1]), False)
        self.assertEqual(array2.has_12([2, 1, 3]), False)
        self.assertEqual(array2.has_12([2, 1, 3, 2]), True)
        self.assertEqual(array2.has_12([2]), False)
        self.assertEqual(array2.has_12([3, 2]), False)
        self.assertEqual(array2.has_12([3, 1, 3, 2]), True)
        self.assertEqual(array2.has_12([3, 5, 9]), False)
        self.assertEqual(array2.has_12([3, 5, 1]),  False)
        self.assertEqual(array2.has_12([3, 2, 1]), False)
        self.assertEqual(array2.has_12([1, 2]), True)
    
    def test_mod_three(self):
        self.assertEqual(array2.mod_three([2, 1, 3, 5]), True)
        self.assertEqual(array2.mod_three([2, 1, 2, 5]), False)
        self.assertEqual(array2.mod_three([2, 4, 2, 5]), True)
        self.assertEqual(array2.mod_three([1, 2, 1, 2, 1]), False)
        self.assertEqual(array2.mod_three([9, 9, 9]), True)
        self.assertEqual(array2.mod_three([1, 2, 1]), False)
        self.assertEqual(array2.mod_three([1, 2]), False)
        self.assertEqual(array2.mod_three([1]), False)
        self.assertEqual(array2.mod_three([]), False)
        self.assertEqual(array2.mod_three([9, 7, 2, 9]), False)
        self.assertEqual(array2.mod_three([9, 7, 2, 9, 2, 2]), False)
        self.assertEqual(array2.mod_three([9, 7, 2, 9, 2, 2, 6]), True)
    
    def test_have_three(self):
        self.assertEqual(array2.have_three([3, 1, 3, 1, 3]), True)
        self.assertEqual(array2.have_three([3, 1, 3, 3]), False)
        self.assertEqual(array2.have_three([3, 4, 3, 3, 4]), False)
        self.assertEqual(array2.have_three([1, 3, 1, 3, 1, 2]), False)
        self.assertEqual(array2.have_three([1, 3, 1, 3, 1, 3]), True)
        self.assertEqual(array2.have_three([1, 3, 3, 1, 3]), False)
        self.assertEqual(array2.have_three([1, 3, 1, 3, 1, 3, 4, 3]), False)
        self.assertEqual(array2.have_three([3, 4, 3, 4, 3, 4, 4]), True)
        self.assertEqual(array2.have_three([3, 3, 3]), False)
        self.assertEqual(array2.have_three([1, 3]), False)
        self.assertEqual(array2.have_three([3]), False)
        self.assertEqual(array2.have_three([1]), False)
    
    def test_two_two(self):
        self.assertEqual(array2.two_two([4, 2, 2, 3]), True)
        self.assertEqual(array2.two_two([2, 2, 4]), True)
        self.assertEqual(array2.two_two([2, 2, 4, 2]), False)
        self.assertEqual(array2.two_two([1, 3, 4]), True)
        self.assertEqual(array2.two_two([1, 2, 2, 3, 4]), True)
        self.assertEqual(array2.two_two([1, 2, 3, 4]), False)
        self.assertEqual(array2.two_two([2, 2]), True)
        self.assertEqual(array2.two_two([2, 2, 7]), True)
        self.assertEqual(array2.two_two([2, 2, 7, 2, 1]), False)
        self.assertEqual(array2.two_two([4, 2, 2, 2]), True)
        self.assertEqual(array2.two_two([2, 2, 2]), True)
        self.assertEqual(array2.two_two([1, 2]), False)
        self.assertEqual(array2.two_two([2]), False)
        self.assertEqual(array2.two_two([1]), True)
        self.assertEqual(array2.two_two([]), True)
        self.assertEqual(array2.two_two([5, 2, 2, 3]), True)
        self.assertEqual(array2.two_two([2, 2, 5, 2]), False)
    
    def test_same_ends(self):
        self.assertEqual(array2.same_ends([5, 6, 45, 99, 13, 5, 6], 1), False)
        self.assertEqual(array2.same_ends([5, 6, 45, 99, 13, 5, 6], 2), True)
        self.assertEqual(array2.same_ends([5, 6, 45, 99, 13, 5, 6], 3), False)
        self.assertEqual(array2.same_ends([1, 2, 5, 2, 1], 1), True)
        self.assertEqual(array2.same_ends([1, 2, 5, 2, 1], 2), False)
        self.assertEqual(array2.same_ends([1, 2, 5, 2, 1], 0), True)
        self.assertEqual(array2.same_ends([1, 2, 5, 2, 1], 5), True)
        self.assertEqual(array2.same_ends([1, 1, 1], 0), True)
        self.assertEqual(array2.same_ends([1, 1, 1], 1), True)
        self.assertEqual(array2.same_ends([1, 1, 1], 2), True)
        self.assertEqual(array2.same_ends([1, 1, 1], 3), True)
        self.assertEqual(array2.same_ends([1], 1), True)
        self.assertEqual(array2.same_ends([], 0), True)
        self.assertEqual(array2.same_ends([4, 2, 4, 5], 1), False)
    
    def test_triple_up(self):
        self.assertEqual(array2.triple_up([1, 4, 5, 6, 2]), True)
        self.assertEqual(array2.triple_up([1, 2, 3]), True)
        self.assertEqual(array2.triple_up([1, 2, 4]), False)
        self.assertEqual(array2.triple_up([1, 2, 4, 5, 7, 6, 5, 6, 7, 6]), True)
        self.assertEqual(array2.triple_up([1, 2, 4, 5, 7, 6, 5, 7, 7, 6]), False)
        self.assertEqual(array2.triple_up([1, 2]), False)
        self.assertEqual(array2.triple_up([1]), False)
        self.assertEqual(array2.triple_up([]), False)
        self.assertEqual(array2.triple_up([10, 9, 8, -100, -99, -98, 100]), True)
        self.assertEqual(array2.triple_up([10, 9, 8, -100, -99, 99, 100]), False)
        self.assertEqual(array2.triple_up([-100, -99, -99, 100, 101, 102]), True)
        self.assertEqual(array2.triple_up([2, 3, 5, 6, 8, 9, 2, 3]), False)
    
    def test_fizz_array_3(self):
        self.assertEqual(array2.fizz_array_3(5, 10), [5, 6, 7, 8, 9])
        self.assertEqual(array2.fizz_array_3(11, 18), [11, 12, 13, 14, 15, 16, 17])
        self.assertEqual(array2.fizz_array_3(1, 3), [1, 2])
        self.assertEqual(array2.fizz_array_3(1, 2), [1])
        self.assertEqual(array2.fizz_array_3(1, 1), [])
        self.assertEqual(array2.fizz_array_3(1000, 1005),  [1000, 1001, 1002, 1003, 1004])

    def test_shift_left(self):
        self.assertEqual(array2.shift_left([6, 2, 5, 3]), [2, 5, 3, 6])
        self.assertEqual(array2.shift_left([1, 2]), [2, 1])
        self.assertEqual(array2.shift_left([1]), [1])
        self.assertEqual(array2.shift_left([]), [])
        self.assertEqual(array2.shift_left([1, 1, 2, 2, 4]), [1, 2, 2, 4, 1])
        self.assertEqual(array2.shift_left([1, 1, 1]), [1, 1, 1])
        self.assertEqual(array2.shift_left([1, 2, 3]), [2, 3, 1])
    
    def test_ten_run(self):
        self.assertEqual(array2.ten_run([2, 10, 3, 4, 20, 5]), [2, 10, 10, 10, 20, 20])
        self.assertEqual(array2.ten_run([10, 1, 20, 2]), [10, 10, 20, 20])
        self.assertEqual(array2.ten_run([10, 1, 9, 20]), [10, 10, 10, 20])
        self.assertEqual(array2.ten_run([1, 2, 50, 1]), [1, 2, 50, 50])
        self.assertEqual(array2.ten_run([1, 20, 50, 1]), [1, 20, 50, 50])
        self.assertEqual(array2.ten_run([10, 10]), [10, 10])
        self.assertEqual(array2.ten_run([10, 2]), [10, 10])
        self.assertEqual(array2.ten_run([0, 2]), [0, 0])
        self.assertEqual(array2.ten_run([1, 2]), [1, 2])
        self.assertEqual(array2.ten_run([1]), [1])
        self.assertEqual(array2.ten_run([]), [])
    
    def test_pre_4(self):
        self.assertEqual(array2.pre_4([1, 2, 4, 1]), [1, 2])
        self.assertEqual(array2.pre_4([3, 1, 4]), [3, 1])
        self.assertEqual(array2.pre_4([1, 4, 4]), [1])
        self.assertEqual(array2.pre_4([1, 4, 4, 2]), [1])
        self.assertEqual(array2.pre_4([1, 3, 4, 2, 4]), [1, 3])
        self.assertEqual(array2.pre_4([4, 4]), [])
        self.assertEqual(array2.pre_4([3, 3, 4]), [3, 3])
        self.assertEqual(array2.pre_4([1, 2, 1, 4]), [1, 2, 1])
        self.assertEqual(array2.pre_4([2, 1, 4, 2]), [2, 1])
        self.assertEqual(array2.pre_4([2, 1, 2, 1, 4, 2]), [2, 1, 2, 1])
    
    def test_post_4(self):
        self.assertEqual(array2.post_4([2, 4, 1, 2]), [1, 2])
        self.assertEqual(array2.post_4([4, 1, 4, 2]), [2])
        self.assertEqual(array2.post_4([4, 4, 1, 2, 3]), [1, 2, 3])
        self.assertEqual(array2.post_4([4, 2]), [2])
        self.assertEqual(array2.post_4([4, 4, 3]), [3])
        self.assertEqual(array2.post_4([4, 4]), [])
        self.assertEqual(array2.post_4([4]), [])
        self.assertEqual(array2.post_4([2, 4, 1, 4, 3, 2]), [3, 2])
        self.assertEqual(array2.post_4([4, 1, 4, 2, 2, 2]), [2, 2, 2])
        self.assertEqual(array2.post_4([3, 4, 3, 2]), [3, 2])
    
    def test_not_alone(self):
        self.assertEqual(array2.not_alone([1, 2, 3], 2), [1, 3, 3])
        self.assertEqual(array2.not_alone([1, 2, 3, 2, 5, 2], 2), [1, 3, 3, 5, 5, 2])
        self.assertEqual(array2.not_alone([3, 4], 3), [3, 4])
        self.assertEqual(array2.not_alone([3, 3], 3), [3, 3])
        self.assertEqual(array2.not_alone([1, 3, 1, 2], 1), [1, 3, 3, 2])
        self.assertEqual(array2.not_alone([3], 3), [3])
        self.assertEqual(array2.not_alone([], 3), [])
        self.assertEqual(array2.not_alone([7, 1, 6], 1), [7, 7, 6]	)
        self.assertEqual(array2.not_alone([1, 1, 1], 1), [1, 1, 1])
        self.assertEqual(array2.not_alone([1, 1, 1, 2], 1), [1, 1, 1, 2])
    
    def test_zero_front(self):
        self.assertEqual(array2.zero_front([1, 0, 0, 1]), [0, 0, 1, 1])
        self.assertEqual(array2.zero_front([0, 1, 1, 0, 1]), [0, 0, 1, 1, 1])
        self.assertEqual(array2.zero_front([1, 0]), [0, 1])
        self.assertEqual(array2.zero_front([0, 1]), [0, 1])
        self.assertEqual(array2.zero_front([1, 1, 1, 0]), [0, 1, 1, 1])
        self.assertEqual(array2.zero_front([2, 2, 2, 2]), [2, 2, 2, 2])
        self.assertEqual(array2.zero_front([0, 0, 1, 0]), [0, 0, 0, 1])
        self.assertEqual(array2.zero_front([-1, 0, 0, -1, 0]), [0, 0, 0, -1, -1])
        self.assertEqual(array2.zero_front([0, -3, 0, -3]), [0, 0, -3, -3])
        self.assertEqual(array2.zero_front([]), [])
        self.assertEqual(array2.zero_front([9, 9, 0, 9, 0, 9]), [0, 0, 9, 9, 9, 9])
    
    def test_without_ten(self):
        self.assertEqual(array2.without_ten([1, 10, 10, 2]), [1, 2, 0, 0])
        self.assertEqual(array2.without_ten([10, 2, 10]), [2, 0, 0])
        self.assertEqual(array2.without_ten([1, 99, 10]), [1, 99, 0])
        self.assertEqual(array2.without_ten([10, 13, 10, 14]), [13, 14, 0, 0])
        self.assertEqual(array2.without_ten([10, 13, 10, 14, 10]), [13, 14, 0, 0, 0])
        self.assertEqual(array2.without_ten([10, 10, 3]), [3, 0, 0])
        self.assertEqual(array2.without_ten([1]), [1])
        self.assertEqual(array2.without_ten([13, 1]), [13, 1])
        self.assertEqual(array2.without_ten([10]), [0])
        self.assertEqual(array2.without_ten([]), [])
    
    def test_zero_max(self):
        self.assertEqual(array2.zero_max([0, 5, 0, 3]), [5, 5, 3, 3])
        self.assertEqual(array2.zero_max([0, 4, 0, 3]), [3, 4, 3, 3])
        self.assertEqual(array2.zero_max([0, 1, 0]), [1, 1, 0])
        self.assertEqual(array2.zero_max([0, 1, 5]), [5, 1, 5])
        self.assertEqual(array2.zero_max([0, 2, 0]), [0, 2, 0])
        self.assertEqual(array2.zero_max([1]), [1])
        self.assertEqual(array2.zero_max([0]), [0])
        self.assertEqual(array2.zero_max([]), [])
        self.assertEqual(array2.zero_max([7, 0, 4, 3, 0, 2]), [7, 3, 4, 3, 0, 2])
        self.assertEqual(array2.zero_max([7, 0, 4, 3, 0, 1]), [7, 3, 4, 3, 1, 1])
        self.assertEqual(array2.zero_max([7, 0, 4, 3, 0, 0]), [7, 3, 4, 3, 0, 0])
        self.assertEqual(array2.zero_max([7, 0, 1, 0, 0, 7]), [7, 7, 1, 7, 7, 7])
    
    def test_even_odd(self):
        self.assertEqual(array2.even_odd([1, 0, 1, 0, 0, 1, 1]), [0, 0, 0, 1, 1, 1, 1])
        self.assertEqual(array2.even_odd([3, 3, 2]), [2, 3, 3])
        self.assertEqual(array2.even_odd([2, 2, 2]), [2, 2, 2])
        self.assertEqual(array2.even_odd([3, 2, 2]), [2, 2, 3])
        self.assertEqual(array2.even_odd([1, 1, 0, 1, 0]), [0, 0, 1, 1, 1])
        self.assertEqual(array2.even_odd([1]), [1])
        self.assertEqual(array2.even_odd([1, 2]), [2, 1])
        self.assertEqual(array2.even_odd([2, 1]), [2, 1])
        self.assertEqual(array2.even_odd([]), [])

    def test_fizz_buzz(self):
        self.assertEqual(array2.fizz_buzz(1, 6), ['1', '2', 'Fizz', '4', 'Buzz'])
        self.assertEqual(array2.fizz_buzz(1, 8), ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7'])
        self.assertEqual(array2.fizz_buzz(1, 11), ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz'])
        self.assertEqual(array2.fizz_buzz(1, 16), ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz'])
        self.assertEqual(array2.fizz_buzz(1, 4), ['1', '2', 'Fizz'])
        self.assertEqual(array2.fizz_buzz(1, 2), ['1'])
        self.assertEqual(array2.fizz_buzz(50, 56), ['Buzz', 'Fizz', '52', '53', 'Fizz', 'Buzz'])
        self.assertEqual(array2.fizz_buzz(15, 17),  ['FizzBuzz', '16'])
        self.assertEqual(array2.fizz_buzz(30, 36), ['FizzBuzz', '31', '32', 'Fizz', '34', 'Buzz'])
        self.assertEqual(array2.fizz_buzz(1000, 1006), ['Buzz', '1001', 'Fizz', '1003', '1004', 'FizzBuzz'])
        self.assertEqual(array2.fizz_buzz(99, 102), ['Fizz', 'Buzz', '101'])
        self.assertEqual(array2.fizz_buzz(14, 20), ['14', 'FizzBuzz', '16', '17', 'Fizz', '19'])

if __name__ == '__main__':
    unittest.main()