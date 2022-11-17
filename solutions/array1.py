# Given an array of ints, return true if 6 appears as either the first 
# or last element in the array. The array will be length 1 or more.
def first_last_6(nums):
    return nums[0] == 6 or nums[-1] == 6

# Given an array of ints, return true if the array is length 1 or more, 
# and the first element and the last element are equal.
def same_first_last(nums):
    return len(nums) > 0 and nums[0] == nums[-1]

# Return an int array length 3 containing the first 3 digits of pi, [3, 1, 4].
def make_pi():
    return [3, 1, 4]

# Given 2 arrays of ints, a and b, return true if they have the same first element 
# or they have the same last element. Both arrays will be length 1 or more.
def common_end(a, b):
    return a[0] == b[0] or a[-1] == b[-1]

# Given an array of ints length 3, return the sum of all the elements.
def sum3(nums):
    return sum(nums)

# Given an array of ints length 3, return an array with the elements "rotated left" 
# so [1, 2, 3] yields [2, 3, 1].
def rotate_left_3(nums):
    return nums[1:] + nums[0:1]

# Given an array of ints length 3, return a new array with the elements in reverse order, 
# so [1, 2, 3] becomes [3, 2, 1].
def reverse_3(nums):
    return list(reversed(nums))

# Given an array of ints length 3, figure out which is larger, the first or last element in 
# the array, and set all the other elements to be that value. Return the changed array.
def max_end_3(nums):
    return [max(nums[0], nums[-1])] * len(nums)

# Given an array of ints, return the sum of the first 2 elements in the array. If the array 
# length is less than 2, just sum up the elements that exist, returning 0 if the array is 
# length 0.
def sum_2(nums):
    return sum(nums[:2])

# Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their 
# middle elements.
def middle_way(a, b):
    return [a[1], b[1]]

# Given an array of ints, return a new array length 2 containing the first and last elements 
# from the original array. The original array will be length 1 or more.
def make_ends(nums):
    return [nums[0], nums[-1]]

# Given an int array length 2, return true if it contains a 2 or a 3.
def has_23(nums):
    return (2 in nums) or (3 in nums)

# Given an int array length 2, return true if it does not contain a 2 or 3.
def no_23(nums):
    return not ((2 in nums) or (3 in nums))

# Given an int array, return a new array with double the length where its last 
# element is the same as the original array, and all the other elements are 0. 
# The original array will be length 1 or more. Note: by default, a new int array 
# contains all 0's.
def make_last(nums):
    return ((( len(nums) * 2) - 1) * [0]) + [nums[-1]]

# Given an int array, return true if the array contains 2 twice, or 3 twice. The array 
# will be length 0, 1, or 2.
def double_23(nums):
    return nums.count(2) == 2 or nums.count(3) == 2