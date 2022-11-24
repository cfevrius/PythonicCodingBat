import sys
sys.path.append('')

import unittest
import solutions.logic1 as logic1

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

if __name__ == '__main__':
    unittest.main()