import unittest
import source.logic1 as logic1

class Logic1Test(unittest.TestCase):
    def test_cigar_party(self):
        self.assertEqual(logic1.cigar_party(30, False), False)
        self.assertEqual(logic1.cigar_party(50, False), True)
        self.assertEqual(logic1.cigar_party(70, True), True)
        self.assertEqual(logic1.cigar_party(30, True), False)
        self.assertEqual(logic1.cigar_party(50, True), True)
        self.assertEqual(logic1.cigar_party(60, False), True)
        self.assertEqual(logic1.cigar_party(61, False), False)
        self.assertEqual(logic1.cigar_party(40, False), True)
        self.assertEqual(logic1.cigar_party(39, False), False)
        self.assertEqual(logic1.cigar_party(40, True), True)
        self.assertEqual(logic1.cigar_party(39, True), False)
    
    def test_date_fasion(self):
        self.assertEqual(logic1.date_fashion(5, 10), 2)
        self.assertEqual(logic1.date_fashion(5, 2), 0)
        self.assertEqual(logic1.date_fashion(5, 5), 1)
        self.assertEqual(logic1.date_fashion(3, 3), 1)
        self.assertEqual(logic1.date_fashion(10, 2), 0)
        self.assertEqual(logic1.date_fashion(2, 9), 0)
        self.assertEqual(logic1.date_fashion(9, 9), 2)
        self.assertEqual(logic1.date_fashion(10, 5), 2)
        self.assertEqual(logic1.date_fashion(2, 2), 0)
        self.assertEqual(logic1.date_fashion(3, 7), 1)
        self.assertEqual(logic1.date_fashion(2, 7), 0)
        self.assertEqual(logic1.date_fashion(6, 2), 0)

    def test_squirrel_play(self):
        self.assertEqual(logic1.squirrel_play(70, False),True)
        self.assertEqual(logic1.squirrel_play(95, False), False)
        self.assertEqual(logic1.squirrel_play(95, True), True)
        self.assertEqual(logic1.squirrel_play(90, False), True)
        self.assertEqual(logic1.squirrel_play(90, True), True)
        self.assertEqual(logic1.squirrel_play(50, False), False)
        self.assertEqual(logic1.squirrel_play(50, True), False)
        self.assertEqual(logic1.squirrel_play(100, False), False)
        self.assertEqual(logic1.squirrel_play(100, True), True)
        self.assertEqual(logic1.squirrel_play(105, True), False)
        self.assertEqual(logic1.squirrel_play(59, False), False)
        self.assertEqual(logic1.squirrel_play(59, True), False)
        self.assertEqual(logic1.squirrel_play(60, False), True)
    
    def test_caught_speeding(self):
        self.assertEqual(logic1.caught_speeding(60, False), 0)
        self.assertEqual(logic1.caught_speeding(65, False), 1)
        self.assertEqual(logic1.caught_speeding(65, True), 0)
        self.assertEqual(logic1.caught_speeding(80, False), 1)
        self.assertEqual(logic1.caught_speeding(85, False), 2)
        self.assertEqual(logic1.caught_speeding(85, True), 1)
        self.assertEqual(logic1.caught_speeding(70, False), 1)
        self.assertEqual(logic1.caught_speeding(75, False), 1)
        self.assertEqual(logic1.caught_speeding(75, True), 1)
        self.assertEqual(logic1.caught_speeding(40, False), 0)
        self.assertEqual(logic1.caught_speeding(40, True), 0)
        self.assertEqual(logic1.caught_speeding(90, False), 2)
    
    def test_sorta_sum(self):
        self.assertEqual(logic1.sorta_sum(3, 4), 7)
        self.assertEqual(logic1.sorta_sum(9, 4), 20)
        self.assertEqual(logic1.sorta_sum(10, 11), 21)
        self.assertEqual(logic1.sorta_sum(12, -3), 9)
        self.assertEqual(logic1.sorta_sum(-3, 12), 9)
        self.assertEqual(logic1.sorta_sum(4, 5), 9)
        self.assertEqual(logic1.sorta_sum(4, 6), 20)
        self.assertEqual(logic1.sorta_sum(14, 7), 21)
        self.assertEqual(logic1.sorta_sum(14, 6), 20)
    
    def test_alarm_clock(self):
        self.assertEqual(logic1.alarm_clock(1, False), '7:00') 
        self.assertEqual(logic1.alarm_clock(5, False), '7:00') 
        self.assertEqual(logic1.alarm_clock(0, False), '10:00') 
        self.assertEqual(logic1.alarm_clock(6, False), '10:00') 
        self.assertEqual(logic1.alarm_clock(0, True), 'off') 
        self.assertEqual(logic1.alarm_clock(6, True), 'off') 
        self.assertEqual(logic1.alarm_clock(1, True), '10:00') 
        self.assertEqual(logic1.alarm_clock(3, True), '10:00') 
        self.assertEqual(logic1.alarm_clock(5, True), '10:00') 

    def test_love_6(self):
        self.assertEqual(logic1.love_6(6, 4), True) 
        self.assertEqual(logic1.love_6(4, 5), False) 
        self.assertEqual(logic1.love_6(1, 5), True) 
        self.assertEqual(logic1.love_6(1, 6), True) 
        self.assertEqual(logic1.love_6(1, 8), False) 
        self.assertEqual(logic1.love_6(1, 7), True) 
        self.assertEqual(logic1.love_6(7, 5), False) 
        self.assertEqual(logic1.love_6(8, 2), True) 
        self.assertEqual(logic1.love_6(6, 6), True) 
        self.assertEqual(logic1.love_6(-6, 2), False) 
        self.assertEqual(logic1.love_6(-4, -10), True) 
        self.assertEqual(logic1.love_6(-7, 1), False) 
        self.assertEqual(logic1.love_6(7, -1), True) 
        self.assertEqual(logic1.love_6(-6, 12), True) 
        self.assertEqual(logic1.love_6(-2, -4), False) 
        self.assertEqual(logic1.love_6(7, 1), True) 
        self.assertEqual(logic1.love_6(0, 9), False) 
        self.assertEqual(logic1.love_6(8, 3), False) 
        self.assertEqual(logic1.love_6(3, 3), True) 
        self.assertEqual(logic1.love_6(3, 4), False) 

    def test_in_1_to_10(self):
        self.assertEqual(logic1.in_1_to_10(5, False), True)
        self.assertEqual(logic1.in_1_to_10(11, False), False)
        self.assertEqual(logic1.in_1_to_10(11, True), True)
        self.assertEqual(logic1.in_1_to_10(10, False), True)
        self.assertEqual(logic1.in_1_to_10(10, True), True)
        self.assertEqual(logic1.in_1_to_10(9, False), True)
        self.assertEqual(logic1.in_1_to_10(9, True), False)
        self.assertEqual(logic1.in_1_to_10(1, False), True)
        self.assertEqual(logic1.in_1_to_10(1, True), True)
        self.assertEqual(logic1.in_1_to_10(0, False), False)
        self.assertEqual(logic1.in_1_to_10(0, True), True)
        self.assertEqual(logic1.in_1_to_10(-1, False), False)
        self.assertEqual(logic1.in_1_to_10(-1, True), True)
        self.assertEqual(logic1.in_1_to_10(99, False), False)
        self.assertEqual(logic1.in_1_to_10(-99, True), True)
    
    def test_special_eleven(self):
        self.assertEqual(logic1.special_eleven(22), True)
        self.assertEqual(logic1.special_eleven(23), True)
        self.assertEqual(logic1.special_eleven(24), False)
        self.assertEqual(logic1.special_eleven(21), False)
        self.assertEqual(logic1.special_eleven(11), True)
        self.assertEqual(logic1.special_eleven(12), True)
        self.assertEqual(logic1.special_eleven(10), False)
        self.assertEqual(logic1.special_eleven(9), False)
        self.assertEqual(logic1.special_eleven(8), False)
        self.assertEqual(logic1.special_eleven(0), True)
        self.assertEqual(logic1.special_eleven(1), True)
        self.assertEqual(logic1.special_eleven(2), False)
        self.assertEqual(logic1.special_eleven(121), True)
        self.assertEqual(logic1.special_eleven(122), True)
        self.assertEqual(logic1.special_eleven(123), False)
        self.assertEqual(logic1.special_eleven(46), False)
        self.assertEqual(logic1.special_eleven(49), False)
        self.assertEqual(logic1.special_eleven(52), False)
        self.assertEqual(logic1.special_eleven(54), False)
        self.assertEqual(logic1.special_eleven(55), True)
    
    def  test_more_20(self):
        self.assertEqual(logic1.more_20(20), False)
        self.assertEqual(logic1.more_20(21), True)
        self.assertEqual(logic1.more_20(22), True)
        self.assertEqual(logic1.more_20(23), False)
        self.assertEqual(logic1.more_20(25), False)
        self.assertEqual(logic1.more_20(30), False)
        self.assertEqual(logic1.more_20(31), False)
        self.assertEqual(logic1.more_20(59), False)
        self.assertEqual(logic1.more_20(60), False)
        self.assertEqual(logic1.more_20(61), True)
        self.assertEqual(logic1.more_20(62), True)
        self.assertEqual(logic1.more_20(1020), False)
        self.assertEqual(logic1.more_20(1021), True)
        self.assertEqual(logic1.more_20(1000), False)
        self.assertEqual(logic1.more_20(1001), True)
        self.assertEqual(logic1.more_20(50), False)
        self.assertEqual(logic1.more_20(55), False)
        self.assertEqual(logic1.more_20(40), False)
        self.assertEqual(logic1.more_20(41), True)
        self.assertEqual(logic1.more_20(39), False)
        self.assertEqual(logic1.more_20(42), True)
    
    def test_old_35(self):
        self.assertEqual(logic1.old_35(3), True)
        self.assertEqual(logic1.old_35(10), True)
        self.assertEqual(logic1.old_35(15), False)
        self.assertEqual(logic1.old_35(5), True)
        self.assertEqual(logic1.old_35(9), True)
        self.assertEqual(logic1.old_35(8), False)
        self.assertEqual(logic1.old_35(7), False)
        self.assertEqual(logic1.old_35(6), True)
        self.assertEqual(logic1.old_35(17), False)
        self.assertEqual(logic1.old_35(18), True)
        self.assertEqual(logic1.old_35(29), False)
        self.assertEqual(logic1.old_35(20), True)
        self.assertEqual(logic1.old_35(21), True)
        self.assertEqual(logic1.old_35(22), False)
        self.assertEqual(logic1.old_35(45), False)
        self.assertEqual(logic1.old_35(99), True)
    
    def test_less_20(self):
        self.assertEqual(logic1.less_20(18), True)
        self.assertEqual(logic1.less_20(19), True)
        self.assertEqual(logic1.less_20(20), False)
        self.assertEqual(logic1.less_20(8), False)
        self.assertEqual(logic1.less_20(17), False)
        self.assertEqual(logic1.less_20(23), False)
        self.assertEqual(logic1.less_20(25), False)
        self.assertEqual(logic1.less_20(30), False)
        self.assertEqual(logic1.less_20(31), False)
        self.assertEqual(logic1.less_20(58), True)
        self.assertEqual(logic1.less_20(59), True)
        self.assertEqual(logic1.less_20(60), False)
        self.assertEqual(logic1.less_20(61), False)
        self.assertEqual(logic1.less_20(62), False)
        self.assertEqual(logic1.less_20(1017), False)
        self.assertEqual(logic1.less_20(1018), True)
        self.assertEqual(logic1.less_20(1019), True)
        self.assertEqual(logic1.less_20(1020), False)
        self.assertEqual(logic1.less_20(1021), False)
        self.assertEqual(logic1.less_20(1022), False)
        self.assertEqual(logic1.less_20(1023), False)
        self.assertEqual(logic1.less_20(37), False)
    
    def test_near_ten(self):
        self.assertEqual(logic1.near_ten(12), True)
        self.assertEqual(logic1.near_ten(17), False)
        self.assertEqual(logic1.near_ten(19), True)
        self.assertEqual(logic1.near_ten(31), True)
        self.assertEqual(logic1.near_ten(6), False)
        self.assertEqual(logic1.near_ten(10), True)
        self.assertEqual(logic1.near_ten(11), True)
        self.assertEqual(logic1.near_ten(21), True)
        self.assertEqual(logic1.near_ten(22), True)
        self.assertEqual(logic1.near_ten(23), False)
        self.assertEqual(logic1.near_ten(54), False)
        self.assertEqual(logic1.near_ten(155), False)
        self.assertEqual(logic1.near_ten(158), True)
        self.assertEqual(logic1.near_ten(3), False)
        self.assertEqual(logic1.near_ten(1), True)
    
    def test_teen_sum(self):
        self.assertEqual(logic1.teen_sum(3, 4), 7)
        self.assertEqual(logic1.teen_sum(10, 13), 19)
        self.assertEqual(logic1.teen_sum(13, 2), 19)
        self.assertEqual(logic1.teen_sum(3, 19), 19)
        self.assertEqual(logic1.teen_sum(13, 13), 19)
        self.assertEqual(logic1.teen_sum(10, 10), 20)
        self.assertEqual(logic1.teen_sum(6, 14), 19)
        self.assertEqual(logic1.teen_sum(15, 2), 19)
        self.assertEqual(logic1.teen_sum(19, 19), 19)
        self.assertEqual(logic1.teen_sum(19, 20), 19)
        self.assertEqual(logic1.teen_sum(2, 18), 19)
        self.assertEqual(logic1.teen_sum(12, 4), 16)
        self.assertEqual(logic1.teen_sum(2, 20), 22)
        self.assertEqual(logic1.teen_sum(2, 17), 19)
        self.assertEqual(logic1.teen_sum(2, 16), 19)
        self.assertEqual(logic1.teen_sum(6, 7), 13)
    
    def test_answer_cell(self):
        self.assertEqual(logic1.answer_cell(False, False, False), True)
        self.assertEqual(logic1.answer_cell(False, False, True), False)
        self.assertEqual(logic1.answer_cell(True, False, False), False)
        self.assertEqual(logic1.answer_cell(True, True, False), True)
        self.assertEqual(logic1.answer_cell(False, True, False), True)
        self.assertEqual(logic1.answer_cell(True, True, True), False)
    
    def test_tea_party(self):
        self.assertEqual(logic1.tea_party(6, 8), 1)
        self.assertEqual(logic1.tea_party(3, 8), 0)
        self.assertEqual(logic1.tea_party(20, 6), 2)
        self.assertEqual(logic1.tea_party(12, 6), 2)
        self.assertEqual(logic1.tea_party(11, 6), 1)
        self.assertEqual(logic1.tea_party(11, 4), 0)
        self.assertEqual(logic1.tea_party(4, 5), 0)
        self.assertEqual(logic1.tea_party(5, 5), 1)
        self.assertEqual(logic1.tea_party(6, 6), 1)
        self.assertEqual(logic1.tea_party(5, 10), 2)
        self.assertEqual(logic1.tea_party(5, 9), 1)
        self.assertEqual(logic1.tea_party(10, 4), 0)
        self.assertEqual(logic1.tea_party(10, 20), 2)

    def test_fizz_string(self):
        self.assertEqual(logic1.fizz_string('fig'), 'Fizz')
        self.assertEqual(logic1.fizz_string('dib'), 'Buzz')
        self.assertEqual(logic1.fizz_string('fib'), 'FizzBuzz')
        self.assertEqual(logic1.fizz_string('abc'), 'abc')
        self.assertEqual(logic1.fizz_string('fooo'), 'Fizz')
        self.assertEqual(logic1.fizz_string('booo'), 'booo')
        self.assertEqual(logic1.fizz_string('ooob'), 'Buzz')
        self.assertEqual(logic1.fizz_string('fooob'), 'FizzBuzz')
        self.assertEqual(logic1.fizz_string('f'), 'Fizz')
        self.assertEqual(logic1.fizz_string('b'), 'Buzz')
        self.assertEqual(logic1.fizz_string('abcb'), 'Buzz')
        self.assertEqual(logic1.fizz_string('Hello'), 'Hello')
        self.assertEqual(logic1.fizz_string('Hellob'), 'Buzz')
        self.assertEqual(logic1.fizz_string('af'), 'af')
        self.assertEqual(logic1.fizz_string('bf'), 'bf')
        self.assertEqual(logic1.fizz_string('fb'), 'FizzBuzz')
    
    def test_fizz_string_2(self):
        self.assertEqual(logic1.fizz_string_2(1), '1!')
        self.assertEqual(logic1.fizz_string_2(2), '2!')
        self.assertEqual(logic1.fizz_string_2(3), 'Fizz!')
        self.assertEqual(logic1.fizz_string_2(4), '4!')
        self.assertEqual(logic1.fizz_string_2(5), 'Buzz!')
        self.assertEqual(logic1.fizz_string_2(6), 'Fizz!')
        self.assertEqual(logic1.fizz_string_2(7), '7!')
        self.assertEqual(logic1.fizz_string_2(8), '8!')
        self.assertEqual(logic1.fizz_string_2(9), 'Fizz!')
        self.assertEqual(logic1.fizz_string_2(15), 'FizzBuzz!')
        self.assertEqual(logic1.fizz_string_2(16), '16!')
        self.assertEqual(logic1.fizz_string_2(18), 'Fizz!')
        self.assertEqual(logic1.fizz_string_2(19), '19!')
        self.assertEqual(logic1.fizz_string_2(21), 'Fizz!')
        self.assertEqual(logic1.fizz_string_2(44), '44!')
        self.assertEqual(logic1.fizz_string_2(45), 'FizzBuzz!')
        self.assertEqual(logic1.fizz_string_2(100), 'Buzz!')

    def test_two_as_one(self):
        self.assertEqual(logic1.two_as_one(1, 2, 3), True)
        self.assertEqual(logic1.two_as_one(3, 1, 2), True)
        self.assertEqual(logic1.two_as_one(3, 2, 2), False)
        self.assertEqual(logic1.two_as_one(2, 3, 1), True)
        self.assertEqual(logic1.two_as_one(5, 3, -2), True)
        self.assertEqual(logic1.two_as_one(5, 3, -3), False)
        self.assertEqual(logic1.two_as_one(2, 5, 3), True)
        self.assertEqual(logic1.two_as_one(9, 5, 5), False)
        self.assertEqual(logic1.two_as_one(9, 4, 5), True)
        self.assertEqual(logic1.two_as_one(5, 4, 9), True)
        self.assertEqual(logic1.two_as_one(3, 3, 0), True)
        self.assertEqual(logic1.two_as_one(3, 3, 2), False)

    def test_in_order(self):
        self.assertEqual(logic1.in_order(1, 2, 4, False), True)
        self.assertEqual(logic1.in_order(1, 2, 1, False), False)
        self.assertEqual(logic1.in_order(1, 1, 2, True), True)
        self.assertEqual(logic1.in_order(3, 2, 4, False), False)
        self.assertEqual(logic1.in_order(2, 3, 4, False), True)
        self.assertEqual(logic1.in_order(3, 2, 4, True), True)
        self.assertEqual(logic1.in_order(4, 2, 2, True), False)
        self.assertEqual(logic1.in_order(4, 5, 2, True), False)
        self.assertEqual(logic1.in_order(2, 4, 6, True), True)
        self.assertEqual(logic1.in_order(7, 9, 10, False), True)
        self.assertEqual(logic1.in_order(7, 5, 6, True), True)
        self.assertEqual(logic1.in_order(7, 5, 4, True), False)
    
    def test_in_order_equal(self):
        self.assertEqual(logic1.in_order_equal(2, 5, 11, False), True)
        self.assertEqual(logic1.in_order_equal(5, 7, 6, False), False)
        self.assertEqual(logic1.in_order_equal(5, 5, 7, True), True)
        self.assertEqual(logic1.in_order_equal(5, 5, 7, False), False)
        self.assertEqual(logic1.in_order_equal(2, 5, 4, False), False)
        self.assertEqual(logic1.in_order_equal(3, 4, 3, False), False)
        self.assertEqual(logic1.in_order_equal(3, 4, 4, False), False)
        self.assertEqual(logic1.in_order_equal(3, 4, 3, True), False)
        self.assertEqual(logic1.in_order_equal(3, 4, 4, True), True)
        self.assertEqual(logic1.in_order_equal(1, 5, 5, True), True)
        self.assertEqual(logic1.in_order_equal(5, 5, 5, True), True)
        self.assertEqual(logic1.in_order_equal(2, 2, 1, True), False)
        self.assertEqual(logic1.in_order_equal(9, 2, 2, True), False)
        self.assertEqual(logic1.in_order_equal(0, 1, 0, True), False)
    
    def test_last_digit(self):
        self.assertEqual(logic1.last_digit(23, 19, 13), True)
        self.assertEqual(logic1.last_digit(23, 19, 12), False)
        self.assertEqual(logic1.last_digit(23, 19, 3), True)
        self.assertEqual(logic1.last_digit(23, 19, 39), True)
        self.assertEqual(logic1.last_digit(1, 2, 3), False)
        self.assertEqual(logic1.last_digit(1, 1, 2), True)
        self.assertEqual(logic1.last_digit(1, 2, 2), True)
        self.assertEqual(logic1.last_digit(14, 25, 43), False)
        self.assertEqual(logic1.last_digit(14, 25, 45), True)
        self.assertEqual(logic1.last_digit(248, 106, 1002), False)
        self.assertEqual(logic1.last_digit(248, 106, 1008), True)
        self.assertEqual(logic1.last_digit(10, 11, 20), True)
        self.assertEqual(logic1.last_digit(0, 11, 0), True)
    
    def test_less_by_10(self):
        self.assertEqual(logic1.less_by_10(1, 7, 11), True)
        self.assertEqual(logic1.less_by_10(1, 7, 10), False)
        self.assertEqual(logic1.less_by_10(11, 1, 7), True)
        self.assertEqual(logic1.less_by_10(10, 7, 1), False)
        self.assertEqual(logic1.less_by_10(-10, 2, 2), True)
        self.assertEqual(logic1.less_by_10(2, 11, 11), False)
        self.assertEqual(logic1.less_by_10(3, 3, 30), True)
        self.assertEqual(logic1.less_by_10(3, 3, 3), False)
        self.assertEqual(logic1.less_by_10(10, 1, 11), True)
        self.assertEqual(logic1.less_by_10(10, 11, 1), True)
        self.assertEqual(logic1.less_by_10(10, 11, 2), False)
        self.assertEqual(logic1.less_by_10(3, 30, 3), True)
        self.assertEqual(logic1.less_by_10(2, 2, -8), True)
        self.assertEqual(logic1.less_by_10(2, 8, 12), True)
    
    def test_without_doubles(self):
        self.assertEqual(logic1.without_doubles(2, 3, True), 5)
        self.assertEqual(logic1.without_doubles(3, 3, True), 7)
        self.assertEqual(logic1.without_doubles(3, 3, False), 6)
        self.assertEqual(logic1.without_doubles(2, 3, False), 5)
        self.assertEqual(logic1.without_doubles(5, 4, True), 9)
        self.assertEqual(logic1.without_doubles(5, 4, False), 9)
        self.assertEqual(logic1.without_doubles(5, 5, True), 11)
        self.assertEqual(logic1.without_doubles(5, 5, False), 10)
        self.assertEqual(logic1.without_doubles(6, 6, True), 7)
        self.assertEqual(logic1.without_doubles(6, 6, False), 12)
        self.assertEqual(logic1.without_doubles(1, 6, True), 7)
        self.assertEqual(logic1.without_doubles(6, 1, False), 7)
    
    def test_max_mod_5(self):
        self.assertEqual(logic1.max_mod_5(2, 3), 3)
        self.assertEqual(logic1.max_mod_5(6, 2), 6)
        self.assertEqual(logic1.max_mod_5(3, 2), 3)
        self.assertEqual(logic1.max_mod_5(8, 12), 12)
        self.assertEqual(logic1.max_mod_5(7, 12), 7)
        self.assertEqual(logic1.max_mod_5(11, 6), 6)
        self.assertEqual(logic1.max_mod_5(2, 7), 2)
        self.assertEqual(logic1.max_mod_5(7, 7), 0)
        self.assertEqual(logic1.max_mod_5(9, 1), 9)
        self.assertEqual(logic1.max_mod_5(9, 14), 9)
        self.assertEqual(logic1.max_mod_5(1, 2), 2)
    
    def test_red_ticket(self):
        self.assertEqual(logic1.red_ticket(2, 2, 2), 10	)
        self.assertEqual(logic1.red_ticket(2, 2, 1), 0)
        self.assertEqual(logic1.red_ticket(0, 0, 0), 5)
        self.assertEqual(logic1.red_ticket(2, 0, 0), 1)
        self.assertEqual(logic1.red_ticket(1, 1, 1), 5)
        self.assertEqual(logic1.red_ticket(1, 2, 1), 0)
        self.assertEqual(logic1.red_ticket(1, 2, 0), 1)
        self.assertEqual(logic1.red_ticket(0, 2, 2), 1)
        self.assertEqual(logic1.red_ticket(1, 2, 2), 1)
        self.assertEqual(logic1.red_ticket(0, 2, 0), 0)
        self.assertEqual(logic1.red_ticket(1, 1, 2), 0)
    
    def test_green_ticket(self):
        self.assertEqual(logic1.green_ticket(1, 2, 3), 0)
        self.assertEqual(logic1.green_ticket(2, 2, 2), 20)
        self.assertEqual(logic1.green_ticket(1, 1, 2), 10)
        self.assertEqual(logic1.green_ticket(2, 1, 1), 10)
        self.assertEqual(logic1.green_ticket(1, 2, 1), 10)
        self.assertEqual(logic1.green_ticket(3, 2, 1), 0)
        self.assertEqual(logic1.green_ticket(0, 0, 0), 20)
        self.assertEqual(logic1.green_ticket(2, 0, 0), 10)
        self.assertEqual(logic1.green_ticket(0, 9, 10), 0)
        self.assertEqual(logic1.green_ticket(0, 10, 0), 10)
        self.assertEqual(logic1.green_ticket(9, 9, 9), 20)
        self.assertEqual(logic1.green_ticket(9, 0, 9), 10)
    
    def test_blue_ticket(self):
        self.assertEqual(logic1.blue_ticket(9, 1, 0), 10)
        self.assertEqual(logic1.blue_ticket(9, 2, 0), 0)
        self.assertEqual(logic1.blue_ticket(6, 1, 4), 10)
        self.assertEqual(logic1.blue_ticket(6, 1, 5), 0)
        self.assertEqual(logic1.blue_ticket(10, 0, 0), 10)
        self.assertEqual(logic1.blue_ticket(15, 0, 5), 5)
        self.assertEqual(logic1.blue_ticket(5, 15, 5), 10)
        self.assertEqual(logic1.blue_ticket(4, 11, 1), 5)
        self.assertEqual(logic1.blue_ticket(13, 2, 3), 5)
        self.assertEqual(logic1.blue_ticket(8, 4, 3), 0)
        self.assertEqual(logic1.blue_ticket(8, 4, 2), 10)
        self.assertEqual(logic1.blue_ticket(8, 4, 1), 0)
    
    def test_share_digit(self):
        self.assertEqual(logic1.share_digit(12, 23), True)
        self.assertEqual(logic1.share_digit(12, 43), False)
        self.assertEqual(logic1.share_digit(12, 44), False)
        self.assertEqual(logic1.share_digit(23, 12), True)
        self.assertEqual(logic1.share_digit(23, 39), True)
        self.assertEqual(logic1.share_digit(23, 19), False)
        self.assertEqual(logic1.share_digit(30, 90), True)
        self.assertEqual(logic1.share_digit(30, 91), False)
        self.assertEqual(logic1.share_digit(55, 55), True)
        self.assertEqual(logic1.share_digit(55, 44), False)
    
    def test_sum_limit(self):
        self.assertEqual(logic1.sum_limit(2, 3), 5)
        self.assertEqual(logic1.sum_limit(8, 3), 8)
        self.assertEqual(logic1.sum_limit(8, 1), 9)
        self.assertEqual(logic1.sum_limit(11, 39), 50)
        self.assertEqual(logic1.sum_limit(11, 99), 11)
        self.assertEqual(logic1.sum_limit(0, 0), 0)
        self.assertEqual(logic1.sum_limit(99, 0), 99)
        self.assertEqual(logic1.sum_limit(99, 1), 99)
        self.assertEqual(logic1.sum_limit(123, 1), 124)
        self.assertEqual(logic1.sum_limit(1, 123), 1)
        self.assertEqual(logic1.sum_limit(23, 60), 83)
        self.assertEqual(logic1.sum_limit(23, 80), 23)
        self.assertEqual(logic1.sum_limit(9000, 1), 9001)
        self.assertEqual(logic1.sum_limit(90000000, 1), 90000001)
        self.assertEqual(logic1.sum_limit(9000, 1000), 9000)

if __name__ == '__main__':
    unittest.main()