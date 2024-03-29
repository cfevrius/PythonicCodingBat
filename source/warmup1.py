def sleep_in(weekday, vacation):
    """The parameter weekday is true if it is a weekday, and the parameter vacation is true if 
    we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return true 
    if we sleep in.
    """
    return not weekday or vacation

def monkey_trouble(aSmile, bSmile):
    """We have two monkeys, a and b, and the parameters aSmile and bSmile indicate if each is 
    smiling. We are in trouble if they are both smiling or if neither of them is smiling. 
    Return true if we are in trouble.
    """
    return aSmile and bSmile or (not aSmile and not bSmile)

def sum_double(a, b):
    """Given two int values, return their sum. Unless the two values are the same, then return 
    double their sum.
    """
    result = a + b if a !=b else 2 * (a + b)
    return result

def diff_21(n):
    """Given an int n, return the absolute difference between n and 21, except return double the 
    absolute difference if n is over 21.
    """
    diff = abs(21 - n)
    result = diff if n <= 21 else 2 * diff
    return result

def parrot_trouble(talking, hour):
    """We have a loud talking parrot. The "hour" parameter is the current hour time in the range 
    0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return 
    true if we are in trouble.
    """
    return talking and (hour < 7 or hour > 20)

def makes_10(a, b):
    """Given 2 ints, a and b, return true if one if them is 10 or if their sum is 10."""
    return 10 in {a, b, a + b}

def near_hundred(n):
    """Given an int n, return true if it is within 10 of 100 or 200. 
    """
    return abs(n - 100) <= 10 or abs(n - 200) <= 10

def pos_neg(a, b, negative):
    """Given 2 int values, return true if one is negative and one is positive. Except if the parameter 
    "negative" is true, then return true only if both are negative.
    """
    result = (a < 0 and b < 0) if negative else (a * b) < 0
    return result

def not_string(string):
    """Given a string, return a new string where "not " has been added to the front. However, if 
    the string already begins with "not", return the string unchanged.
    """
    result = f'not {string}' if string[0:3] != "not" else string
    return result

def missing_char(string, n):
    """Given a non-empty string and an int n, return a new string where the char at index n has been 
    removed. The value of n will be a valid index of a char in the original string (i.e. n will be 
    in the range 0..len(string)-1 inclusive).
    """
    return f"{string[:n]}{string[n+1:]}"

def front_back(string):
    """Given a string, return a new string where the first and last chars have been exchanged."""
    return f'{string[-1]}{string[1:-1]}{string[0]}' if len(string) > 1 else string

def front_3(string):
    """Given a string, we'll say that the front is the first 3 chars of the string. If the string 
    length is less than 3, the front is whatever is there. Return a new string which is 3 copies of 
    the front.
    """
    return 3 * string[0:3]

def back_around(string):
    """Given a string, take the last char and return a new string with the last char added at the 
    front and back, so "cat" yields "tcatt". The original string will be length 1 or more.
    """
    back = string[-1]
    return f"{back}{string}{back}"

def or_35(n):
    """Return true if the given non-negative number is a multiple of 3 or a multiple of 5. 
    Use the % "mod" operator.
    """
    return n % 3 == 0 or n % 5 == 0

def front_22(string):
    """Given a string, take the first 2 chars and return the string with the 2 chars added at both 
    the front and back, so "kitten" yields"kikittenki". If the string length is less than 2, use 
    whatever chars are there.
    """
    return f'{string[:2]}{string}{string[0:2]}'

def start_hi(string):
    """Given a string, return true if the string starts with "hi" and false otherwise."""
    return string.startswith('hi')

def icy_hot(temp1, temp2):
    """Given two temperatures, return true if one is less than 0 and the other is greater than 100."""
    def is_icy_hot(x, y):
        return x < 0 and y > 100
    return is_icy_hot(temp1, temp2) or is_icy_hot(temp2, temp1)

def in_1020(a, b):
    """Given 2 int values, return true if either of them is in the range 10..20 inclusive."""
    def in_range(x): return 10 <= x <= 20
    return in_range(a) or in_range(b)

def has_teen(a, b, c):
    """We'll say that a number is "teen" if it is in the range 13..19 inclusive. Given 3 int values, 
    return true if 1 or more of them are teen.
    """
    def is_teen(x): return 13 <= x <= 19
    return is_teen(a) or is_teen(b) or is_teen(c)

def lone_teen(a, b):
    """We'll say that a number is "teen" if it is in the range 13..19 inclusive. Given 2 int values, 
    return true if one or the other is teen, but not both.
    """
    def is_teen(x): return 13 <= x <= 19
    teens = [x for x in [a, b] if is_teen(x)]
    return len(teens) == 1

def del_del(string):
    """Given a string, if the string "del" appears starting at index 1, return a string where that 
    "del" has been deleted. Otherwise, return the string unchanged.
    """
    return f'{string[0]}{string[4:]}' if len(string) >= 4 and string[1:4] == 'del' else string

def mix_start(string):
    """Return true if the given string begins with "mix", except the 'm' can be anything, so "pix", 
    "9ix" .. all count.
    """
    return len(string) >= 3 and string[1:3] == 'ix'

def start_oz(string):
    """Given a string, return a string made of the first 2 chars (if present), however include first 
    char only if it is 'o' and include the second only if it is 'z', so "ozymandias" yields "oz".
    """
    first_char_is_o = string[:1] if string[:1] == 'o' else ''
    second_char_is_z = string[1:2] if string[1:2] == 'z' else ''
    return f"{first_char_is_o}{second_char_is_z}"

def int_max(a, b, c):
    """Given three int values, a b c, return the largest."""
    return max(a, b, c)

def close_10(a, b):
    """Given 2 int values, return whichever value is nearest to the value 10, or return 0 in the event 
    of a tie. 
    """
    a_dist_10 = abs(10 - a)
    b_dist_10 = abs(10 - b)
    return 0 if a_dist_10 == b_dist_10 else (a if a_dist_10 < b_dist_10 else b)

def in_3040(a, b):
    """Given 2 int values, return true if they are both in the range 30..40 inclusive, or they are both 
    in the range 40..50 inclusive.
    """
    def in_30_40(x): return 30 <= x <= 40
    def in_40_50(x): return 40 <= x <= 50
    return (in_30_40(a) and in_30_40(b)) or (in_40_50(a) and in_40_50(b))

def max_1020(a, b):
    """Given 2 positive int values, return the larger value that is in the range 10..20 inclusive, or 
    return 0 if neither is in that range.
    """
    nums_in_range = [x for x in [a, b] if 10 <= x <= 20]
    return max(nums_in_range, default=0)

def string_e(string):
    """Return true if the given string contains between 1 and 3 'e' chars."""
    return 1 <= string.count('e') <= 3

def last_digit(a, b):
    """Given two non-negative int values, return true if they have the same last digit, such as with 27 
    and 57. 
    """
    a_last_digit = a % 10
    b_last_digit = b % 10
    return a_last_digit == b_last_digit

def end_up(string):
    """Given a string, return a new string where the last 3 chars are now in upper case. If the string has 
    less than 3 chars, uppercase whatever is there.
    """
    front = string[:-3]
    end = string[-3:]
    return f"{front}{end.upper()}"

def every_nth(string, n):
    """Given a non-empty string and an int N, return the string made starting with char 0, and then every 
    Nth char of the string. So if N is 3, use char 0, 3, 6, ... and so on. N is 1 or more.
    """
    return string[::n]
