def double_char(string):
    """Given a string, return a string where for every char in the original, there are two chars."""
    return ''.join([c + c for c in string])

def count_hi(string):
    """Return the number of times that the string "hi" appears anywhere in the given string."""
    return string.count('hi')

def cat_dog(string):
    """Return true if the string "cat" and "dog" appear the same number of times in the given string."""
    return string.count('cat') == string.count('dog')

def count_code(string):
    """Return the number of times that the string "code" appears anywhere in the given string, except 
    we'll accept any letter for the 'd', so "cope" and "cooe" count.
    """
    def has_code_at_index(index):
        return all([string[index] == 'c', string[index + 1] == 'o', string[index + 3] == 'e'])

    matches = [i for i, _ in enumerate(string[:-3]) if  has_code_at_index(i)]
    return len(matches)

def end_other(a, b):
    """
    Given two strings, return true if either of the strings appears at the very end of the other string, 
    ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). 
    """
    def does_end(a, b): 
        return a.lower().endswith(b.lower())

    return does_end(a, b) or does_end(b, a)

def xyz_there(string):
    """Return true if the given string contains an appearance of "xyz" where the xyz is not directly preceeded 
    by a period (.). So "xxyz" counts but "x.xyz" does not.
    """
    def has_match_at_index(index):
        return string[index:index+3] == 'xyz' and ((index == 0) or string[index - 1] != '.')

    matches = [i for i, _ in enumerate(string[1:]) if has_match_at_index(i)]
    return len(matches)

def bob_there(string):
    """Return true if the given string contains a "bob" string, but where the middle 'o' char can be any char."""
    def has_match_at_index(i):
        return string[i] == 'b' and string[i+2] == 'b'

    matches = [i for i, _ in enumerate(string[:-2]) if has_match_at_index(i)]
    return len(matches) > 0

def xyz_balance(string):
    """We'll say that a String is xy-balanced if for all the 'x' chars in the string, there exists a 'y' char 
    somewhere later in the string. So "xxy" is balanced, but "xyx" is not. One 'y' can balance multiple 'x's. 
    Return true if the given string is xy-balanced.
    """
    def is_balanced(i):
        return 'y' in string[i:]

    are_xs_balanced = [is_balanced(i) for i, v in enumerate(string) if v == 'x']
    return all(are_xs_balanced)

def mix_string(a, b):
    """Given two strings, a and b, create a bigger string made of the first char of a, the first char of b, the 
    second char of a, the second char of b, and so on. Any leftover chars go at the end of the result.
    """
    front = ''.join([item for tup in zip(a, b) for item in tup])
    shorter, longer = sorted((a, b), key=len)
    end = longer[-(len(longer) - len(shorter)):] if len(longer) > len(shorter) else ''
    return f'{front}{end}'

def repeat_end(string, n):
    """Given a string and an int n, return a string made of n repetitions of the last n characters of the string. 
    You may assume that n is between 0 and the length of the string, inclusive.
    """
    return n * string[-n:]

def repeat_front(string, n):
    """Given a string and an int n, return a string made of the first n characters of the string, followed by the 
    first n-1 characters of the string, and so on. You may assume that n is between 0 and the length of the string, 
    inclusive (i.e. 0 <= n <= len(string)).
    """
    return ''.join([string[:i] for i in reversed(range(1, n+1))])

def repeat_separator(word, sep, count):
    """Given two strings, word and a separator sep, return a big string made of count occurrences of the word, separated 
    by the separator string.
    """
    return sep.join([word] * count)

def prefix_again(string, n):
    """Given a string, consider the prefix string made of the first N chars of the string. Does that prefix string appear 
    somewhere else in the string? Assume that the string is not empty and that N is in the range 1..len(string).
    """
    return string[:n] in string[n:]

def xyz_middle(string):
    """Given a string, does "xyz" appear in the middle of the string? To define middle, we'll say that the number of chars 
    to the left and right of the "xyz" must differ by at most one. This problem is harder than it looks.
    """
    span = 4
    def ceil(x):
        return int(x + 0.5)
    start = ceil( (len(string) / 2) - (span / 2) )
    middle = string[start:start+span]

    # If the length of the string is ODD, the 'xyz' must be at *start* because 
    # there will be the same amount of spaces on either side of 'xyz':
    # 
    # e.g. 'AAAxyzBBB'
    # 
    # So the 'xyz' string MUST be exactly in the middle.
    # Even numbers can be anywhere in span.
    if len(string) % 2 == 1:
        return string[start:start+3] =='xyz'
    else:
        return 'xyz' in middle

def get_sandwich(string):
    """A sandwich is two pieces of bread with something in between. Return the string that is between the first and last 
    appearance of "bread" in the given string, or return the empty string "" if there are not two pieces of bread.
    """
    sandwich_indices = [i for i, _ in enumerate(string[:-4]) if string[i:i+5] == 'bread']
    if len(sandwich_indices) > 1:
        first, last = sandwich_indices[0], sandwich_indices[-1]
        return string[first + 5:last]
    return ""

def same_star_char(string):
    """Returns true if for every '*' (star) in the string, if there are chars both immediately before and after the star, 
    they are the same.
    """
    def is_valid(i):
        return (not 0 < i < (len(string) - 1)) or (string[i-1] == string[i+1])

    are_stars_valid = [is_valid(i) for i, v in enumerate(string) if v == '*']
    return all(are_stars_valid)

def one_two(string):
    """Given a string, compute a new string by moving the first char to come after the next two chars, so "abc" yields "bca". 
    Repeat this process for each subsequent group of 3 chars, so "abcdef" yields "bcaefd". Ignore any group of fewer than 
    3 chars at the end.
    """
    groups_of_3 = [string[i:i+3]
                   for i, _ in enumerate(string)
                   if i % 3 == 0 and len(string[i:i+3]) >= 3]
    updated_front = ''.join(map(lambda string: string[1:] + string[0], groups_of_3))
    return updated_front

def zip_zap(string):
    """Look for patterns like "zip" and "zap" in the string -- length-3, starting with 'z' and ending with 'p'. Return a string 
    where for all such words, the middle letter is gone, so "zipXzap" yields "zpXzp".
    """
    indices_to_remove = [i 
                         for i, _ in enumerate(string) 
                         if 0 < i < (len(string) - 1) and string[i-1] == 'z' and string[i+1] == 'p']
    return ''.join([char for i, char in enumerate(string) if i not in indices_to_remove])

def star_out(string):
    """Return a version of the given string, where for every star (*) in the string the star and the chars immediately to its left 
    and right are gone. So "ab*cd" yields "ad" and "ab**cd" also yields "ad".
    """
    nested_indices_to_remove = [(i - 1, i, i + 1)
                         for i, v in enumerate(string)
                         if v == '*']

    flattened_indices_to_remove = [item for tup in nested_indices_to_remove for item in tup]
    return ''.join([char for i, char in enumerate(string) if i not in flattened_indices_to_remove]) 

def plus_out(string, word):
    """Given a string and a non-empty word string, return a version of the original String where all chars have been replaced by pluses 
    ("+"), except for appearances of the word string which are preserved unchanged.
    """
    word_len = len(word)
    nested_indices_to_ignore = [range(i,i+word_len) for i, v in enumerate(string) if string[i:i+word_len] == word]
    flattened_indices_to_ignore = [num for seq in nested_indices_to_ignore for num in seq]
    return ''.join([v if i in flattened_indices_to_ignore else '+' for i, v in enumerate(string)])
    
def word_ends(string, word):
    """
    Given a string and a non-empty word string, return a string made of each char just before and just after every appearance of the 
    word in the string. Ignore cases where there is no char before or after the word, and a char may be included twice if it is between 
    two words.
    """
    word_len = len(word)
    def get_char_at_index(i):
        return string[i] if 0 <= i <= len(string) - 1 else ''

    chars_before_and_after_match = [f'{get_char_at_index(i - 1)}{get_char_at_index(i + word_len)}'
                                    for i, v in enumerate(string) 
                                    if string[i : i + word_len] == word]
    return ''.join(chars_before_and_after_match)
