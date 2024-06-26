# Purpose: starting at some index (current index + 1), find the index of the smallest element in the list
# Input Types: list[int], int (which represents the current index)
# Output Type: int
# Example Inputs: [1,7,9,5,4,2], 1
# Example Output: 5

#def find_idx_of_smallest(some_list, current_idx):
    #idx_of_min = current_idx
    #start_idx = current_idx + 1
    #for idx in range():
      #  if some_list[idx] < some_list[idx_of_min]:



# Purpose: sorts, in place, the elements of a list using the selection sort algorithm
# Input Type: list[int]
# Output Type: None (because nothing is returned, the list is sorted in place)
# Example Input: [2, 7, 9, 5, 4, 1]
# Example Output: None

#def selection_sort(some_list):
  #  for idx in range(len(some_list) - 1):
       # idx_of_min = find_idx_of_smallest()
     #   current_element = some_list[idx]
    #    some_list[idx] = some_list[idx_of_min]
    #    some_list[idx_of_min] = current_element

# ~~~~~~~

# Purpose: extracts a substring, given the start of the substring in the full string list
#          and the number of words that make up the substring
#          (substring represents a possible match to the substring we are searching for)
# Input: list[str], int, int
# Output: list[str]
# Example Input: ["I", "love", "Harry", "Potter"], 2, 5
# Example Output: ["Harry", "Potter"]

def extract_possible_match(some_list, len_old_list, start_idx):
    if start_idx + len_old_list > len(some_list):
        return None
    possible_match = []
    for idx in range(len_old_list):
        possible_match.append(some_list[idx + start_idx])
    return possible_match

def replace(some_list, replace_list, start_idx):
    for idx in range(len(replace_list)):
        some_list[idx + start_idx] = replace_list[idx]


# Purpose: replace a given substring within a given string,
#          with a new given substring (the two substrings should
#          have the same number of words)
# Input: str (representing the full string), str (representing substring to replace), str (representing replacing substring)
# Output: str (representing full string but with substrings replaced)
# Example Input: "I love Harry Potter because Harry Potter is the best", "Harry Potter", "Star Wars"
# Example Output: "I love Star Wars because Star Wars is the best"

def replace_substring(full_string, substring_old, substring_new):
    full_string_list = full_string.split(" ")
    substring_old_list = substring_old.split(" ")
    substring_new_list = substring_new.split(" ")

    if len(substring_old_list) != len(substring_new_list):
        return "The two substrings do not have the same number of words!"

    for idx in range(len(full_string_list)):
        if full_string_list[idx] == substring_old_list[0]:
            possible_match = extract_possible_match(full_string_list, len(substring_old_list), idx)
            if possible_match == substring_old_list:
                replace(full_string_list, substring_new_list, idx)

    new_string_to_return = " ".join(full_string_list)
    return new_string_to_return

full_string = "I love Harry Potter because Harry Potter is the best Harry"
old_substring = "Harry Potter"
new_substring = "Star Wars"
new_string = replace_substring(full_string, old_substring, new_substring)
print(new_string)


# Purpose: Given a string, for each letter that appears in the string,
#          count the number of times it appears
# Input: str
# Output: dict
# Example Input: "Hello World"
# Example Output: {"H": 1, "E": 1, "L": 3, "O": 2, "W": 1, "R": 1, "D": 1}

def histogram_letters(some_string):
    hist = {}
    for letter in some_string:
        if letter not in hist:
            hist[letter] = 1
        else:
           hist[letter] = 1 + hist[letter]