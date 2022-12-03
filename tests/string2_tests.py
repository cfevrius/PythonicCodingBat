import sys
sys.path.append('')

import unittest
import solutions.string2 as string2

class TestsString2(unittest.TestCase):
    def test_double_char(self):
        self.assertEqual(string2.double_char('The'), 'TThhee')
        self.assertEqual(string2.double_char('AAbb'), 'AAAAbbbb')
        self.assertEqual(string2.double_char('Hi-There'), 'HHii--TThheerree')
        self.assertEqual(string2.double_char('Word!'), 'WWoorrdd!!')
        self.assertEqual(string2.double_char('!!'), '!!!!')
        self.assertEqual(string2.double_char(''), '')
        self.assertEqual(string2.double_char('a'), 'aa')
        self.assertEqual(string2.double_char('.'), '..')
        self.assertEqual(string2.double_char('aa'), 'aaaa')
    
    def test_count_hi(self):
        self.assertEqual(string2.count_hi('abc hi ho'), 1)
        self.assertEqual(string2.count_hi('ABChi hi'), 2)
        self.assertEqual(string2.count_hi('hihi'), 2)
        self.assertEqual(string2.count_hi('hiHIhi'), 2)
        self.assertEqual(string2.count_hi(''), 0)
        self.assertEqual(string2.count_hi('h'), 0)
        self.assertEqual(string2.count_hi('hi'), 1)
        self.assertEqual(string2.count_hi('Hi is no HI on ahI'), 0)
        self.assertEqual(string2.count_hi('hiho not HOHIhi'), 2)
    
    def test_cat_dog(self):
        self.assertEqual(string2.cat_dog('catdog'), True)
        self.assertEqual(string2.cat_dog('catcat'), False)
        self.assertEqual(string2.cat_dog('1cat1cadodog'), True)
        self.assertEqual(string2.cat_dog('catxxdogxxxdog'), False)
        self.assertEqual(string2.cat_dog('catxdogxdogxcat'), True)
        self.assertEqual(string2.cat_dog('catxdogxdogxca'), False)
        self.assertEqual(string2.cat_dog('dogdogcat'), False)
        self.assertEqual(string2.cat_dog('dogogcat'), True)
        self.assertEqual(string2.cat_dog('dog'), False)
        self.assertEqual(string2.cat_dog('cat'), False)
        self.assertEqual(string2.cat_dog('ca'), True)
        self.assertEqual(string2.cat_dog('c'), True)
        self.assertEqual(string2.cat_dog(''), True)
    
    def test_count_code(self):
        self.assertEqual(string2.count_code('aaacodebbb'), 1)
        self.assertEqual(string2.count_code('codexxcode'), 2)
        self.assertEqual(string2.count_code('cozexxcope'), 2)
        self.assertEqual(string2.count_code('cozfxxcope'), 1)
        self.assertEqual(string2.count_code('xxcozeyycop'), 1)
        self.assertEqual(string2.count_code('cozcop'), 0)
        self.assertEqual(string2.count_code('abcxyz'), 0)
        self.assertEqual(string2.count_code('code'), 1)
        self.assertEqual(string2.count_code('ode'), 0)
        self.assertEqual(string2.count_code('c'), 0)
        self.assertEqual(string2.count_code(''), 0)
        self.assertEqual(string2.count_code('AAcodeBBcoleCCccoreDD'), 3)
        self.assertEqual(string2.count_code('AAcodeBBcoleCCccorfDD'), 2)
        self.assertEqual(string2.count_code('coAcodeBcoleccoreDD'), 3)
    
    def test_end_other(self):
        self.assertEqual(string2.end_other('Hiabc', 'abc'), True)
        self.assertEqual(string2.end_other('AbC', 'HiaBc'), True)
        self.assertEqual(string2.end_other('abc', 'abXabc'), True)
        self.assertEqual(string2.end_other('Hiabc', 'abcd'), False)
        self.assertEqual(string2.end_other('Hiabc', 'bc'), True)
        self.assertEqual(string2.end_other('Hiabcx', 'bc'), False)
        self.assertEqual(string2.end_other('abc', 'abc'), True)
        self.assertEqual(string2.end_other('xyz', '12xyz'), True)
        self.assertEqual(string2.end_other('yz', '12xz'), False)
        self.assertEqual(string2.end_other('Z', '12xz'), True)
        self.assertEqual(string2.end_other('12', '12'), True)
        self.assertEqual(string2.end_other('abcXYZ', 'abcDEF'), False)
        self.assertEqual(string2.end_other('ab', 'ab12'), False)
        self.assertEqual(string2.end_other('ab', '12ab'), True)
    
    def test_xyz_there(self):
        self.assertEqual(string2.xyz_there('abcxyz'), True)
        self.assertEqual(string2.xyz_there('abc.xyz'), False)
        self.assertEqual(string2.xyz_there('xyz.abc'), True)
        self.assertEqual(string2.xyz_there('abcxy'), False)
        self.assertEqual(string2.xyz_there('xyz'), True)
        self.assertEqual(string2.xyz_there('xy'), False)
        self.assertEqual(string2.xyz_there('x'), False)
        self.assertEqual(string2.xyz_there(''), False)
        self.assertEqual(string2.xyz_there('abc.xyzxyz'), True)
        self.assertEqual(string2.xyz_there('abc.xxyz'), True)
        self.assertEqual(string2.xyz_there('.xyz'), False)
        self.assertEqual(string2.xyz_there('12.xyz'), False)
        self.assertEqual(string2.xyz_there('12xyz'), True)
        self.assertEqual(string2.xyz_there('1.xyz.xyz2.xyz'), False)
    
    def test_bob_there(self):
        self.assertEqual(string2.bob_there('abcbob'), True)
        self.assertEqual(string2.bob_there('b9b'), True)
        self.assertEqual(string2.bob_there('bac'), False)
        self.assertEqual(string2.bob_there('bbb'), True)
        self.assertEqual(string2.bob_there('abcdefb'), False)
        self.assertEqual(string2.bob_there('123abcbcdbabxyz'), True)
        self.assertEqual(string2.bob_there('b12'), False)
        self.assertEqual(string2.bob_there('b1b'), True)
        self.assertEqual(string2.bob_there('b12b1b'), True)
        self.assertEqual(string2.bob_there('bbc'), False)
        self.assertEqual(string2.bob_there('bbb'), True)
        self.assertEqual(string2.bob_there('bb'), False)
        self.assertEqual(string2.bob_there('b'), False)
    
    def test_xyz_balance(self):
        self.assertEqual(string2.xyz_balance('aaxbby'), True)
        self.assertEqual(string2.xyz_balance('aaxbb'), False)
        self.assertEqual(string2.xyz_balance('yaaxbb'), False)
        self.assertEqual(string2.xyz_balance('yaaxbby'), True)
        self.assertEqual(string2.xyz_balance('xaxxbby'), True)
        self.assertEqual(string2.xyz_balance('xaxxbbyx'), False)
        self.assertEqual(string2.xyz_balance('xxbxy'), True)
        self.assertEqual(string2.xyz_balance('xxbx'), False)
        self.assertEqual(string2.xyz_balance('bbb'), True)
        self.assertEqual(string2.xyz_balance('bxbb'), False)
        self.assertEqual(string2.xyz_balance('bxyb'), True)
        self.assertEqual(string2.xyz_balance('xy'), True)
        self.assertEqual(string2.xyz_balance('y'), True)
        self.assertEqual(string2.xyz_balance('x'), False)
        self.assertEqual(string2.xyz_balance(''), True)
        self.assertEqual(string2.xyz_balance('yxyxyxyx'), False)
        self.assertEqual(string2.xyz_balance('yxyxyxyxy'), True)
        self.assertEqual(string2.xyz_balance('12xabxxydxyxyzz'), True)

    def test_mix_string(self):
        self.assertEqual(string2.mix_string('abc', 'xyz'), 'axbycz')
        self.assertEqual(string2.mix_string('Hi', 'There'), 'HTihere')
        self.assertEqual(string2.mix_string('xxxx', 'There'), 'xTxhxexre')
        self.assertEqual(string2.mix_string('xxx', 'X'), 'xXxx')
        self.assertEqual(string2.mix_string('2/', '27 around'), '22/7 around')
        self.assertEqual(string2.mix_string('', 'Hello'), 'Hello')
        self.assertEqual(string2.mix_string('Abc', ''),  'Abc')
        self.assertEqual(string2.mix_string('', ''), '')
        self.assertEqual(string2.mix_string('a', 'b'), 'ab')
        self.assertEqual(string2.mix_string('ax', 'b'), 'abx')
        self.assertEqual(string2.mix_string('a', 'bx'), 'abx')
        self.assertEqual(string2.mix_string('So', 'Long'),  'SLoong')
        self.assertEqual(string2.mix_string('Long', 'So'), 'LSoong')
    
    def test_repeat_end(self):
        self.assertEqual(string2.repeat_end('Hello', 3), 'llollollo')
        self.assertEqual(string2.repeat_end('Hello', 2), 'lolo')
        self.assertEqual(string2.repeat_end('Hello', 1), 'o')
        self.assertEqual(string2.repeat_end('Hello', 0), '')
        self.assertEqual(string2.repeat_end('abc', 3), 'abcabcabc')
        self.assertEqual(string2.repeat_end('1234', 2), '3434')
        self.assertEqual(string2.repeat_end('1234', 3), '234234234')
        self.assertEqual(string2.repeat_end('', 0), '')
    
    def test_repeat_front(self):
        self.assertEqual(string2.repeat_front('Chocolate', 4), 'ChocChoChC')
        self.assertEqual(string2.repeat_front('Chocolate', 3), 'ChoChC')
        self.assertEqual(string2.repeat_front('Ice Cream', 2), 'IcI')
        self.assertEqual(string2.repeat_front('Ice Cream', 1), 'I')
        self.assertEqual(string2.repeat_front('Ice Cream', 0), '')
        self.assertEqual(string2.repeat_front('xyz', 3), 'xyzxyx')
        self.assertEqual(string2.repeat_front('', 0), '')
        self.assertEqual(string2.repeat_front('Java', 4), 'JavaJavJaJ')
        self.assertEqual(string2.repeat_front('Java', 1),  'J')
    
    def test_repeat_separator(self):
        self.assertEqual(string2.repeat_separator('Word', 'X', 3), 'WordXWordXWord')
        self.assertEqual(string2.repeat_separator('This', 'And', 2), 'ThisAndThis')
        self.assertEqual(string2.repeat_separator('This', 'And', 1), 'This')
        self.assertEqual(string2.repeat_separator('Hi', '-n-', 2), 'Hi-n-Hi')
        self.assertEqual(string2.repeat_separator('AAA', '', 1), 'AAA')
        self.assertEqual(string2.repeat_separator('AAA', '', 0), '')
        self.assertEqual(string2.repeat_separator('A', 'B', 5), 'ABABABABA')
        self.assertEqual(string2.repeat_separator('abc', 'XX', 3), 'abcXXabcXXabc')
        self.assertEqual(string2.repeat_separator('abc', 'XX', 2), 'abcXXabc')
        self.assertEqual(string2.repeat_separator('abc', 'XX', 1),  'abc')
        self.assertEqual(string2.repeat_separator('XYZ', 'a', 2), 'XYZaXYZ')
    
    def test_prefix_again(self):
        self.assertEqual(string2.prefix_again('abXYabc', 1), True)
        self.assertEqual(string2.prefix_again('abXYabc', 2), True)
        self.assertEqual(string2.prefix_again('abXYabc', 3), False)
        self.assertEqual(string2.prefix_again('xyzxyxyxy', 2), True)
        self.assertEqual(string2.prefix_again('xyzxyxyxy', 3), False)
        self.assertEqual(string2.prefix_again('Hi12345Hi6789Hi10', 1), True)
        self.assertEqual(string2.prefix_again('Hi12345Hi6789Hi10', 2), True)
        self.assertEqual(string2.prefix_again('Hi12345Hi6789Hi10', 3), True)
        self.assertEqual(string2.prefix_again('Hi12345Hi6789Hi10', 4), False)
        self.assertEqual(string2.prefix_again('a', 1), False)
        self.assertEqual(string2.prefix_again('aa', 1), True)
        self.assertEqual(string2.prefix_again('ab', 1), False)
    
    def test_xyz_middle(self):
        self.assertEqual(string2.xyz_middle('AAxyzBB'), True)
        self.assertEqual(string2.xyz_middle('AxyzBB'), True)
        self.assertEqual(string2.xyz_middle('AxyzBBB'), False)
        self.assertEqual(string2.xyz_middle('AxyzBBBB'), False)
        self.assertEqual(string2.xyz_middle('AAAxyzB'), False)
        self.assertEqual(string2.xyz_middle('AAAxyzBB'), True)
        self.assertEqual(string2.xyz_middle('AAAAxyzBB'), False)
        self.assertEqual(string2.xyz_middle('AAAAAxyzBBB'), False)
        self.assertEqual(string2.xyz_middle('1x345xyz12x4'), True)
        self.assertEqual(string2.xyz_middle('xyzAxyzBBB'), True)
        self.assertEqual(string2.xyz_middle('xyzAxyzBxyz'), True)
        self.assertEqual(string2.xyz_middle('xyzxyzAxyzBxyzxyz'), True)
        self.assertEqual(string2.xyz_middle('xyzxyzxyzBxyzxyz'), True)
        self.assertEqual(string2.xyz_middle('xyzxyzAxyzxyzxyz'), True)
        self.assertEqual(string2.xyz_middle('xyzxyzAxyzxyzxy'), True)
        self.assertEqual(string2.xyz_middle('AxyzxyzBB'), False)
        self.assertEqual(string2.xyz_middle(''), False)
        self.assertEqual(string2.xyz_middle('x'), False)
        self.assertEqual(string2.xyz_middle('xy'), False)
        self.assertEqual(string2.xyz_middle('xyz'), True)
        self.assertEqual(string2.xyz_middle('xyzz'), True)
    
    def test_get_sandwich(self):
        self.assertEqual(string2.get_sandwich('breadjambread'), 'jam')
        self.assertEqual(string2.get_sandwich('xxbreadjambreadyy'), 'jam')
        self.assertEqual(string2.get_sandwich('xxbreadyy'),  '')
        self.assertEqual(string2.get_sandwich('xxbreadbreadjambreadyy'), 'breadjam')
        self.assertEqual(string2.get_sandwich('breadAbread'), 'A')
        self.assertEqual(string2.get_sandwich('breadbread'), '')
        self.assertEqual(string2.get_sandwich('abcbreaz'), '')
        self.assertEqual(string2.get_sandwich('xyz'), '')
        self.assertEqual(string2.get_sandwich(''), '')
        self.assertEqual(string2.get_sandwich('breadbreaxbread'), 'breax')
        self.assertEqual(string2.get_sandwich('breaxbreadybread'), 'y')
        self.assertEqual(string2.get_sandwich('breadbreadbreadbread'), 'breadbread')
    
    def test_same_star_char(self):
        self.assertEqual(string2.same_star_char('xy*yzz'), True)
        self.assertEqual(string2.same_star_char('xy*zzz'), False)
        self.assertEqual(string2.same_star_char('*xa*az'), True)
        self.assertEqual(string2.same_star_char('*xa*bz'), False)
        self.assertEqual(string2.same_star_char('*xa*a*'), True)
        self.assertEqual(string2.same_star_char(''), True)
        self.assertEqual(string2.same_star_char('*xa*a*a'), True)
        self.assertEqual(string2.same_star_char('*xa*a*b'), False)
        self.assertEqual(string2.same_star_char('*12*2*2'), True)
        self.assertEqual(string2.same_star_char('12*2*3*'), False)
        self.assertEqual(string2.same_star_char('abcDEF'), True)
        self.assertEqual(string2.same_star_char('XY*YYYY*Z*'), False)
        self.assertEqual(string2.same_star_char('XY*YYYY*Y*'), True)
        self.assertEqual(string2.same_star_char('12*2*3*'), False)
        self.assertEqual(string2.same_star_char('*'), True)
        self.assertEqual(string2.same_star_char('**'), True)
    
    def test_one_two(self):
        self.assertEqual(string2.one_two('abc'), 'bca')
        self.assertEqual(string2.one_two('tca'), 'cat')
        self.assertEqual(string2.one_two('tcagdo'), 'catdog')
        self.assertEqual(string2.one_two('chocolate'), 'hocolctea')
        self.assertEqual(string2.one_two('1234567890'),'231564897')
        self.assertEqual(string2.one_two('xabxabxabxabxabxabxab'), 'abxabxabxabxabxabxabx')
        self.assertEqual(string2.one_two('abcdefx'), 'bcaefd')
        self.assertEqual(string2.one_two('abcdefxy'), 'bcaefd')
        self.assertEqual(string2.one_two('abcdefxyz'), 'bcaefdyzx')
        self.assertEqual(string2.one_two(''), '')
        self.assertEqual(string2.one_two('x'), '')
        self.assertEqual(string2.one_two('xy'), '')
        self.assertEqual(string2.one_two('xyz'), 'yzx')
        self.assertEqual(string2.one_two('abcdefghijklkmnopqrstuvwxyz1234567890'), 'bcaefdhigkljmnkpqostrvwuyzx231564897')
        self.assertEqual(string2.one_two('abcdefghijklkmnopqrstuvwxyz123456789'), 'bcaefdhigkljmnkpqostrvwuyzx231564897')
        self.assertEqual(string2.one_two('abcdefghijklkmnopqrstuvwxyz12345678'), 'bcaefdhigkljmnkpqostrvwuyzx231564')
    
    def test_zip_zap(self):
        self.assertEqual(string2.zip_zap('zipXzap'), 'zpXzp')
        self.assertEqual(string2.zip_zap('zopzop'), 'zpzp')
        self.assertEqual(string2.zip_zap('zzzopzop'), 'zzzpzp')
        self.assertEqual(string2.zip_zap('zibzap'), 'zibzp')
        self.assertEqual(string2.zip_zap('zip'), 'zp')
        self.assertEqual(string2.zip_zap('zi'), 'zi')
        self.assertEqual(string2.zip_zap('z'), 'z')
        self.assertEqual(string2.zip_zap(''), '')
        self.assertEqual(string2.zip_zap('zzp'), 'zp')
        self.assertEqual(string2.zip_zap('abcppp'), 'abcppp')
        self.assertEqual(string2.zip_zap('azbcppp'), 'azbcppp')
        self.assertEqual(string2.zip_zap('azbcpzpp'), 'azbcpzp')
    
    def test_star_out(self):
        self.assertEqual(string2.star_out('ab*cd'), 'ad')
        self.assertEqual(string2.star_out('ab**cd'), 'ad')
        self.assertEqual(string2.star_out('sm*eilly'), 'silly')
        self.assertEqual(string2.star_out('sm*eil*ly'), 'siy')
        self.assertEqual(string2.star_out('sm**eil*ly'), 'siy')
        self.assertEqual(string2.star_out('sm***eil*ly'), 'siy')
        self.assertEqual(string2.star_out('stringy*'), 'string')
        self.assertEqual(string2.star_out('*stringy'), 'tringy')
        self.assertEqual(string2.star_out('*str*in*gy'), 'ty')
        self.assertEqual(string2.star_out('abc'), 'abc')
        self.assertEqual(string2.star_out('a*bc'), 'c')
        self.assertEqual(string2.star_out('ab'), 'ab')
        self.assertEqual(string2.star_out('a*b'), '')
        self.assertEqual(string2.star_out('a'), 'a')
        self.assertEqual(string2.star_out('a*'),  '')
        self.assertEqual(string2.star_out('*a'),  '')
        self.assertEqual(string2.star_out('*'),  '')
        self.assertEqual(string2.star_out(''),  '')
    
    def test_plus_out(self):
        self.assertEqual(string2.plus_out('12xy34', 'xy'), '++xy++')
        self.assertEqual(string2.plus_out('12xy34', '1'), '1+++++')
        self.assertEqual(string2.plus_out('12xy34xyabcxy', 'xy'), '++xy++xy+++xy')
        self.assertEqual(string2.plus_out('abXYabcXYZ', 'ab'), 'ab++ab++++')
        self.assertEqual(string2.plus_out('abXYabcXYZ', 'abc'), '++++abc+++')
        self.assertEqual(string2.plus_out('abXYabcXYZ', 'XY'), '++XY+++XY+')
        self.assertEqual(string2.plus_out('abXYxyzXYZ', 'XYZ'), '+++++++XYZ')
        self.assertEqual(string2.plus_out('--++ab', '++'), '++++++')
        self.assertEqual(string2.plus_out('aaxxxxbb', 'xx'), '++xxxx++')
        self.assertEqual(string2.plus_out('123123', '3'), '++3++3')
    
    def test_word_ends(self):
        self.assertEqual(string2.word_ends('abcXY123XYijk', 'XY'), 'c13i')
        self.assertEqual(string2.word_ends('XY123XY', 'XY'), '13')
        self.assertEqual(string2.word_ends('XY1XY', 'XY'), '11')
        self.assertEqual(string2.word_ends('XYXY', 'XY'), 'XY')
        self.assertEqual(string2.word_ends('XY', 'XY'), '')
        self.assertEqual(string2.word_ends('Hi', 'XY'), '')
        self.assertEqual(string2.word_ends('', 'XY'), '')
        self.assertEqual(string2.word_ends('abc1xyz1i1j', '1'), 'cxziij')
        self.assertEqual(string2.word_ends('abc1xyz1', '1'), 'cxz')
        self.assertEqual(string2.word_ends('abc1xyz11', '1'),  'cxz11')
        self.assertEqual(string2.word_ends('abc1xyz1abc', 'abc'), '11')
        self.assertEqual(string2.word_ends('abc1xyz1abc', 'b'), 'acac')
        self.assertEqual(string2.word_ends('abc1abc1abc', 'abc'), '1111')

if __name__ == '__main__':
    unittest.main()