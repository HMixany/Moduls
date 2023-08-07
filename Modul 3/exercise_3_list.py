my_list = list()
empty_list = []
not_empty_list = [1, 2, "user"]
some_iterable = ["a", "b", "c"]
first_letter = some_iterable[0]     # first_letter = some_iterable[-3]
middle_one = some_iterable[1]       # middle_one = some_iterable[-2]
last_letter = some_iterable[2]      # last_letter = some_iterable[-1]
some_iterable[1] = 'Z'
print(some_iterable)                # ["a", "Z", "c"]
some_str = "This is awesome string"
first_five = some_str[0:5]
print(first_five)                   # This
numbers = list(range(1, 11))
print(numbers)                      # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = numbers[0:9:2]        # [1, 3, 5, 7, 9]
even_numbers = numbers[1:9:2]       # [2, 4, 6, 8]
three_numbers = numbers[2:9:3]      # [3, 6, 9]
print(f"{odd_numbers} \n {even_numbers} \n {three_numbers}")
first_three = numbers[0:3]          # [1, 2, 3]
numbers_copy = numbers[:]           #
numbers.append(11)                  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
numbers_copy.clear()
numbers.remove(11)
print(numbers)                      # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
chars = ['a', 'b', 'c']
last = chars.pop(1)
print(chars)                        # ['a', 'c']
print(last)                         # 'b'
chars.extend(numbers)
print(chars)                        # ['a', 'c', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
c_ind = chars.index('c')
print(c_ind)                        # 1
chars.append('a')
a_count = chars.count('a')
print(a_count)                      # 2
numbers.sort()
print(numbers)
chars.reverse()
print(chars)
my_list = [5,7,1,9,2,4]
new_list = sorted(my_list)
print(my_list)
print(new_list)

from copy import deepcopy
