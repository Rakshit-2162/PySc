# -*- coding: utf-8 -*-
"""Day2_Assesment.ipynb

# **LIST**

Basic
"""

# 1 - List Creation: Create a list of your five favorite fruits and print them.

favorite_fruits = ["Mango", "Apple", "Banana", "Orange", "Grapes"]
favorite_fruits

# 2 - Sum of Numbers: Write a program that takes a list of numbers and returns the sum of all the numbers.

def sum_of_numbers(numbers):
  total = 0
  for number in numbers:
    total += number
  return total

number_list = [10, 20, 30, 40, 50]
sum_result = sum_of_numbers(number_list)
print(f"sum = {sum_result}")

# 3 - Find Maximum: Given a list of integers, write a function to find and return the maximum number in the list.

def find_maximum(nums):
  if not nums:
    return None
  max = nums[0]
  for i in nums:
    if i > max:
      max = i
  return max

l = [12, 56, 76, 34, 62, 98]
max_num = find_maximum(l)
print(f"Maximum = {max_num}")

# 4 - Count Occurrences: Create a list of words and write a function that counts how many times each word appears in the list.

def count_occurrences(words):
  word_count = {}
  for w in words:
    if w in word_count:
      word_count[w] += 1
    else:
      word_count[w] = 1
  return word_count

word_list = ["apple", "banana", "apple", "orange", "banana", "apple", "grapes"]
result = count_occurrences(word_list)
print(result)

# 5 - Reverse a List: Write a function that takes a list and returns a new list that is the reverse of the original.

def reverse_list(nums):
  return nums[::-1]

arr = [1, 2, 3, 4, 5]
rev = reverse_list(arr)
print(rev)

"""Intermediate"""

# 1 - Unique Elements: Write a function that takes a list and returns a new list containing only the unique elements from the original list.

def unique_elements(nums):
  unique = []
  for i in nums:
    if i not in unique:
      unique.append(i)
  return unique

dup = [1, 3, 4, 1, 2, 4, 8, 6, 4, 3]
unique_list = unique_elements(dup)
print(unique_list)

# 2 - Sorting: Implement a function that sorts a list of integers in ascending order without using built-in sort functions

def sort_list(nums):
  for i in range(len(nums)):
    for j in range(len(nums)):
      if nums[i] < nums[j]:
        nums[i], nums[j] = nums[j], nums[i]
  return nums

unsorted = [5, 2, 8, 1, 9, 3, 7, 4, 6]
sorted_list = sort_list(unsorted)
print(sorted_list)

# 3 - List Comprehension: Use list comprehension to create a list of squares of even numbers from a given list of integers.

def square_even(nums):
  return [i**2 for i in nums if i % 2 == 0]

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = square_even(l)
print(result)

# 4 - Merge Lists: Write a function that takes two lists and merges them into a single list, removing duplicates.

def merge_lists(list1, list2):
  merged = list(set(list1 + list2))
  return merged

l1 = [1, 2, 3, 4, 5]
l2 = [3, 4, 5, 6, 7]
result = merge_lists(l1, l2)
print(result)

# 5 - Palindrome Check: Create a function that checks if a given string is a palindrome (reads the same forwards and backwards).

def is_palindrome(st):
  return st == st[::-1]

word = "malayalam"
result = is_palindrome(word)
print(result)

"""Advanced"""

# 1 - Nested List Flattening: Write a function that takes a nested list (a list of lists) and flattens it into a single list.

def flatten_list(nested_list):
  flat_list = []
  for sublist in nested_list:
    for item in sublist:
      flat_list.append(item)
  return flat_list

l = [[1, 2], [2, 3], [3, 4], [4, 5, 6, 7]]
flatten = flatten_list(l)
print(flatten)

# 2 - Anagram Detection: Create a function that checks if two strings are anagrams of each other (contain the same characters in a different order).

def is_anagram(str1, str2):
  str1 = str1.lower()
  str2 = str2.lower()
  return sorted(str1) == sorted(str2)

word1 = "listen"
word2 = "silent"
result = is_anagram(word1, word2)
print(result)

# 3 - Fibonacci Sequence: Write a function that generates the first n numbers of the Fibonacci sequence and returns them as a list.

def fibonacci(n):
  fib_list = [0, 1]
  while len(fib_list) < n:
    next_num = fib_list[-1] + fib_list[-2]
    fib_list.append(next_num)
  return fib_list

n = 10
result = fibonacci(n)
print(result)

# 4 - Sublist Search: Given a list and a sublist, write a function that checks if the sublist exists within the list.

def is_sublist(lst, sublst):
  for i in range(len(lst) - len(sublst) + 1):
    if lst[i:i+len(sublst)] == sublst:
      return True
  return False

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sub = [3, 4, 5]
result = is_sublist(l, sub)
print(result)

# 5 - Frequency Dictionary: Create a function that takes a list of integers and returns a dictionary with the frequency of each integer in the list.

def frequency_dict(nums):
  freq_dict = {}
  for num in nums:
    if num in freq_dict:
      freq_dict[num] += 1
    else:
      freq_dict[num] = 1
  return freq_dict

d = [1, 2, 6, 7, 7, 2, 1, 8, 3, 4, 4, 3, 5]
result = frequency_dict(d)
print(result)

"""# **DICTIONARY**

Basic
"""

# 1 - Create a Dictionary: Create a dictionary that contains the names of three people as keys and their ages as values. Print the dictionary.

name = {'Rakshit': 22,
        'Jishnu': 23,
        'Shrikant': 24}
name

# 2 - Accessing Values: Given a dictionary of a person's details (name, age, city), write a function to print the person's name and city.

def print_name_city(person_details):
  if 'name' in person_details and 'city' in person_details:
    print("Name:", person_details['name'])
    print("City:", person_details['city'])
  else:
    print("Details are not available.")

person_info = {'name': 'Rakshit', 'age': 22, 'city': 'Bangalore'}
print_name_city(person_info)

# 3 - Add a Key-Value Pair: Start with an empty dictionary and add a key-value pair (e.g., "color": "blue"). Print the updated dictionary.

dir = {}

dir['color'] = 'blue'
dir['name'] = 'Ram'
dir['age'] = 20

dir

# 4 - Remove a Key-Value Pair: Given a dictionary, remove a specific key (e.g., "age") and print the updated dictionary.

del dir['age']

dir

# 5 - Check Key Existence: Write a function that checks if a specific key exists in a given dictionary and returns True or False.

def check(dir, key):
  return key in dir

print(check(dir, 'name'))

"""Internediate"""

# 1 - Merge Two Dictionaries: Write a function that takes two dictionaries and merges them into one. If there are duplicate keys, sum their values.

def merge(dir1, dir2):
  merged = dir1.copy()
  for key, value in dir2.items():
    if key in merged:
      merged[key] += value
    else:
      merged[key] = value
  return merged

a = {'mango': 12, 'orange': 10, 'apple': 6}
b = {'banana': 16, 'apple': 4, 'mango': 8, 'pinapple': 3}

merged = merge(a, b)
merged

# 2 - Count Character Frequency: Write a function that takes a string and returns a dictionary with the frequency of each character in the string.

def character_frequency(input_string):
    frequency = {}
    for char in input_string:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency

string = "hellothisisrakshit"
freq = character_frequency(string)
print(freq)

# 3 - Invert a Dictionary: Given a dictionary where values are unique, write a function to invert the dictionary (swap keys and values).

def invert_dictionary(input_dict):
  inverted_dict = {}
  for key, value in input_dict.items():
    if value in inverted_dict:
      print("Values in the dictionary are not unique.")
      return None
    inverted_dict[value] = key
  return inverted_dict

original = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
inverted = invert_dictionary(original)
print(inverted)

# 4 - Filter Dictionary: Write a function that takes a dictionary and a threshold value, returning a new dictionary that only includes items with values greater than the threshold.

def filter_dictionary(input_dict, threshold):
  filtered_dict = {}
  for key, value in input_dict.items():
    if value > threshold:
      filtered_dict[key] = value
  return filtered_dict

input = {'first': 89, 'second': 76, 'third': 90, 'fourth': 79}
filtered = filter_dictionary(input, 80)
print(filtered)

# 5 - Dictionary Comprehension: Use dictionary comprehension to create a dictionary where the keys are numbers from 1 to 10 and the values are their squares.

squares_dict = {num: num**2 for num in range(1, 11)}
squares_dict

"""Advanced"""

# 1 - Group by Key: Given a list of tuples (name, age), write a function that groups the names by age in a dictionary.
def group_by_age(people):
    age_groups = {}
    for name, age in people:
        if age not in age_groups:
            age_groups[age] = []
        age_groups[age].append(name)
    return age_groups

people = [("Alice", 25), ("Bob", 30), ("Charlie", 25), ("David", 35)]
grouped_people = group_by_age(people)
print(grouped_people)

# 2 - Nested Dictionary: Create a nested dictionary to represent a school with classes as keys and a list of student names as values. Write a function to add a student to a specific class.
def add_student(school, class_name, student_name):
    if class_name not in school:
        school[class_name] = []
    school[class_name].append(student_name)
    return school

school = {
    "Math": ["Alice", "Bob"],
    "Science": ["Charlie", "David"]}
new_school = add_student(school, "Math", "Eve")
print(new_school)

# 3 - Find the Most Frequent Value: Write a function that takes a dictionary and returns the key with the highest value. If there are ties, return all keys with the highest value.
def most_frequent_value(data):
    if not data:
        return None

    max_value = max(data.values())
    most_frequent_keys = [key for key, value in data.items() if value == max_value]
    return most_frequent_keys

most = most_frequent_value(squares_dict)
most

# 4 - Deep Merge Dictionaries: Write a function that merges two dictionaries deeply, meaning that if a key exists in both dictionaries and its value is also a dictionary, it should merge those dictionaries recursively.

def deep_merge(dict1, dict2):
  merged = dict1.copy()
  for key, value in dict2.items():
    if key in merged and isinstance(merged[key], dict) and isinstance(value, dict):
      merged[key] = deep_merge(merged[key], value)
    else:
      merged[key] = value
  return merged

dict1 = {"a": 1, "b": {"c": 2, "d": 3}, "e": 5}
dict2 = {"b": {"c": 4, "e": 6}, "f": 7}

merged_dict = deep_merge(dict1, dict2)
print(merged_dict)

# 5 - Flatten a Nested Dictionary: Write a function that takes a nested dictionary and flattens it into a single-level dictionary with keys as tuples representing the path to each value. with example

def flatten_dict(nested_dict, parent_key='', sep='_'):
    items = []
    for k, v in nested_dict.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

# Example usage
nested = {'a': 1, 'b': {'c': 2, 'd': {'e': 3}}}
flattened = flatten_dict(nested)
print(flattened)



"""# **TUPLES**

Basic
"""

# 1 - Create a Tuple: Create a tuple containing the names of five countries and print it.
countries = ("USA", "Canada", "UK", "Germany", "France")
print(countries)

# 2 - Accessing Elements: Given a tuple of integers, write a function to return the first and last elements.
def first_last(data):
    return data[0], data[-1]

numbers = (10, 20, 30, 40, 50)
first, last = first_last(numbers)
print(f"First: {first}, Last: {last}")

# 3 - Tuple Length: Write a function that takes a tuple and returns its length.
def tuple_length(data):
    return len(data)

print(f"Length of countries tuple: {tuple_length(countries)}")

# 4 - Count Occurrences: Given a tuple of elements, write a function to count how many times a specific element appears in the tuple.
def count_occurrences(data, element):
    return data.count(element)

mixed_tuple = (1, 2, 2, 3, 4, 2, 5)
print(f"Number of times 2 appears: {count_occurrences(mixed_tuple, 2)}")

# 5 - Convert to List: Write a function that converts a tuple to a list and returns the list.
def tuple_to_list(data):
  return list(data)

my_tuple = (1, 2, 3, 4, 5)
my_list = tuple_to_list(my_tuple)
print(f"Tuple converted to list: {my_list}")

"""Intermediate"""

# 1 - Tuple Unpacking: Write a function that takes a tuple of two elements (name, age) and unpacks it into separate variables.
def unpack_tuple(person_data):
  name, age = person_data
  return name, age

person = ("Alice", 30)
name, age = unpack_tuple(person)
print(f"Name: {name}, Age: {age}")

# 2 - Find Maximum and Minimum: Write a function that takes a tuple of numbers and returns the maximum and minimum values.
def find_max_min(numbers):
  if not numbers:
    return None
  return max(numbers), min(numbers)

number_tuple = (10, 5, 25, 15, 30)
max_val, min_val = find_max_min(number_tuple)
print(f"Maximum: {max_val}, Minimum: {min_val}")

# 3 - Concatenate Tuples: Write a function that takes two tuples and concatenates them into a new tuple.
def concatenate_tuples(tuple1, tuple2):
  return tuple1 + tuple2

tuple_a = (1, 2, 3)
tuple_b = (4, 5, 6)
concatenated_tuple = concatenate_tuples(tuple_a, tuple_b)
print(f"Concatenated tuple: {concatenated_tuple}")

# 4 - Check for Existence: Write a function that checks if a specific element exists in a given tuple and returns True or False.
def element_exists(data, element):
  return element in data

my_tuple = (1, 2, 3, 4, 5)
print(f"Does 3 exist in the tuple? {element_exists(my_tuple, 3)}")
print(f"Does 6 exist in the tuple? {element_exists(my_tuple, 6)}")

# 5 - Slice a Tuple: Write a function that takes a tuple and two indices, and returns a new tuple that is a slice of the original tuple.
def slice_tuple(data, start_index, end_index):
  if not isinstance(data, tuple) or not (0 <= start_index < len(data)) or not (0 <= end_index <= len(data)) or start_index >= end_index:
      return tuple()

  return data[start_index:end_index]

my_tuple = (10, 20, 30, 40, 50, 60)
sliced_tuple = slice_tuple(my_tuple, 2, 5)
print(f"Sliced tuple: {sliced_tuple}")

"""Advanced"""

# 1 - Nested Tuples: Write a function that takes a nested tuple (a tuple containing other tuples) and flattens it into a single tuple.
def flatten_tuple(nested_tuple):
  flattened = []
  for item in nested_tuple:
    if isinstance(item, tuple):
      flattened.extend(flatten_tuple(item))
    else:
      flattened.append(item)
  return tuple(flattened)

nested_t = ((1, 2), (3, 4), (5, (6, 7)))
flat_t = flatten_tuple(nested_t)
print(f"Flattened tuple: {flat_t}")

# 2 - Tuple to Dictionary: Write a function that takes a tuple of key-value pairs and converts it into a dictionary.
def tuple_to_dict(key_value_pairs):
    if not isinstance(key_value_pairs, tuple):
        return {}

    result_dict = {}
    for pair in key_value_pairs:
        if isinstance(pair, tuple) and len(pair) == 2:
            key, value = pair
            result_dict[key] = value

    return result_dict

pairs = (("a", 1), ("b", 2), ("c", 3))
my_dict = tuple_to_dict(pairs)
print(f"Dictionary from tuple: {my_dict}")

# 3 - Find Duplicates: Write a function that takes a tuple and returns a new tuple containing only the duplicate elements.
def find_duplicates(input_tuple):
    counts = {}
    duplicates = []
    for item in input_tuple:
        if item in counts:
            counts[item] += 1
            if counts[item] == 2:
                duplicates.append(item)
        else:
            counts[item] = 1

    return tuple(duplicates)

my_tuple = (1, 2, 2, 3, 4, 4, 5, 1)
duplicate_elements = find_duplicates(my_tuple)
print(f"Duplicate elements: {duplicate_elements}")

# 4 - Rotate a Tuple: Write a function that rotates a tuple by a given number of positions to the right. with example of each
def rotate_tuple(input_tuple, pos):
    n = len(input_tuple)
    pos = pos % n
    rotated_tuple = input_tuple[-pos:] + input_tuple[:-pos]
    return rotated_tuple

my_tuple = (1, 2, 3, 4, 5)
rotated = rotate_tuple(my_tuple, 2)
print(f"Rotated tuple: {rotated}")

# 5 - Tuple Comparison: Write a function that compares two tuples and returns True if they are equal, and False otherwise. with example
def compare_tuples(tuple1, tuple2):
  return tuple1 == tuple2

tuple_a = (1, 2, 3)
tuple_b = (1, 2, 3)
tuple_c = (1, 2, 4)

print(f"tuple_a and tuple_b are equal: {compare_tuples(tuple_a, tuple_b)}")
print(f"tuple_a and tuple_c are equal: {compare_tuples(tuple_a, tuple_c)}")



"""# **SET**

Basic
"""

# 1 - Create a Set: Create a set containing the names of five fruits and print it.
fruits = {"apple", "banana", "orange", "grape", "kiwi"}
print(fruits)

# 2 - Add an Element: Given a set of colors, write a function to add a new color to the set and print the updated set.
def add_color(colors, new_color):
    colors.add(new_color)
    print(colors)

my_colors = {"red", "green", "blue"}
add_color(my_colors, "yellow")

# 3 - Remove an Element: Write a function that removes a specific element from a set if it exists, and print the updated set.
def remove_element(input_set, element):
    if element in input_set:
        input_set.remove(element)
        print(input_set)
    else:
        print(f"{element} not found in the set")

my_set = {1, 2, 3, 4, 5}
remove_element(my_set, 3)
remove_element(my_set, 6)

# 4 - Check Membership: Write a function that checks if a specific element is in a given set and returns True or False.
def check_membership(input_set, element):
  return element in input_set

my_set = {1, 2, 3, 4, 5}
print(check_membership(my_set, 3))
print(check_membership(my_set, 6))

# 5 - Set Length: Write a function that takes a set and returns its length.
def set_length(input_set):
    return len(input_set)

my_set = {1, 2, 3, 4, 5}
print(set_length(my_set))

"""Intermediate"""

# 1 - Union of Sets: Write a function that takes two sets and returns their union.
def set_union(set1, set2):
  return set1 | set2

set_a = {1, 2, 3}
set_b = {3, 4, 5}
union_set = set_union(set_a, set_b)
print(f"Union: {union_set}")

# 2 - Intersection of Sets: Write a function that takes two sets and returns their intersection.
def set_intersection(set1, set2):
  return set1 & set2

set_a = {1, 2, 3}
set_b = {3, 4, 5}
intersection_set = set_intersection(set_a, set_b)
print(f"Intersection: {intersection_set}")

# 3 - Difference of Sets: Write a function that takes two sets and returns the difference (elements in the first set but not in the second).
def set_difference(set1, set2):
  return set1 - set2

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5}
difference_set = set_difference(set_a, set_b)
print(f"Difference of sets (set1 - set2): {difference_set}")

# 4 - Subset Check: Write a function that checks if one set is a subset of another set and returns True or False.
def is_subset(set1, set2):
  return set1.issubset(set2)

set_a = {1, 2}
set_b = {1, 2, 3, 4}
print(f"Is set_a a subset of set_b? {is_subset(set_a, set_b)}")

# 5 - Set Comprehension: Use set comprehension to create a set of squares of even numbers from a given list of integers.
def square_even_numbers(numbers):
  return {n**2 for n in numbers if n % 2 == 0}

numbers = [1, 2, 3, 4, 5, 6]
squares_set = square_even_numbers(numbers)
print(f"Set of squares of even numbers: {squares_set}")

"""Advanced"""

# 1 - Symmetric Difference: Write a function that takes two sets and returns their symmetric difference (elements in either set but not in both).
def symmetric_difference(set1, set2):
  return set1 ^ set2

set1 = {1, 2, 3}
set2 = {3, 4, 5}
symmetric_diff = symmetric_difference(set1, set2)
print(f"Symmetric Difference: {symmetric_diff}")

# 2 - Find Unique Elements: Given a list of elements, write a function that returns a set of unique elements from the list.
def find_unique_elements(data):
  return set(data)

my_list = [1, 2, 2, 3, 4, 4, 5]
unique_elements = find_unique_elements(my_list)
print(f"Unique Elements: {unique_elements}")

# 3 - Count Unique Words: Write a function that takes a string and returns the number of unique words in it.
def count_unique_words(text):
  words = text.lower().split()
  return len(set(words))

text = "this is a test string string"
unique_word_count = count_unique_words(text)
print(f"Unique Word Count: {unique_word_count}")

# 4 - Set Operations on Multiple Sets: Write a function that takes a list of sets and returns the union, intersection, and difference of all.
def set_operations_on_multiple_sets(sets):
    union_result = set.union(*sets)
    print("Union of sets:", union_result)

    intersection_result = set.intersection(*sets)
    print("Intersection of sets:", intersection_result)

    if len(sets) > 0:
        difference_result = sets[0] - set.union(*sets[1:])
        print(f"Difference of sets (sets[0] - others): {difference_result}")

set_a = {1, 2, 3}
set_b = {3, 4, 5}
set_c = {3, 5, 6}
set_operations_on_multiple_sets([set_a,set_b,set_c])

# 5 - Frozenset: Create a frozenset from a list of elements and demonstrate its immutability by attempting to add an element to it. with example
elements = [1, 2, 3, 4, 5]
my_frozenset = frozenset(elements)
print(my_frozenset)

try:
  my_frozenset.add(6)
except AttributeError as e:
    print(e)

