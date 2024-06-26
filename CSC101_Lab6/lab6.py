import data
from typing import Optional

# Write your functions for each part in the space below.

# Part 0

# Finds the index of the smallest value in the list, if there are values,
#     starting from the provided index (if in bounds).
# input: a list of integers
# input: a starting index
# returns: index of the smallest value as an int or None if no value is found
def index_smallest_from(values:list[int], start:int) -> Optional[int]:
    if start >= len(values) or start < 0:
        return None

    index = start
    for idx in range(start + 1, len(values)):
        if values[idx] < values[index]:
            index = idx

    return index


# Sorts, in place, the elements of a list using the selection sort algorithm.
# input: a list of integers
# returns: nothing is returned; the list is sorted in place
#    <This function modifies/mutates the input list. Though a traditional
#     approach, cloning the list sorting the clone is potentially less
#     surprising. Or even using a different sorting algorithm.>
def selection_sort(values:list[int]) -> None:
    for idx in range(len(values) - 1):
        mindex = index_smallest_from(values, idx)
        tmp = values[mindex]
        values[mindex] = values[idx]
        values[idx] = tmp


# Part 1
# Purpose: this function takes a list of data.Book values and reorganizes
#          the list by titles in alphabetical order.
# Input: list[data.Book]
# Output: None
# Example of Input: [data.Book("Harper Lee", "To Kill A Mocking Bird"), data.Book("J.D. Salinger", "The Catcher in the Rye"), data.Book("Ray Bradbury", "Fahrenheit 451")]
# Example of Output: [data.Book("Ray Bradbury", "Fahrenheit 451"), data.Book("J.D. Salinger", "The Catcher in the Rye"), data.Book("Harper Lee", "To Kill A Mocking Bird")]

def selection_sort_books(list_in: list[data.Book]) -> list[data.Book]:
    for idx in range(len(list_in)):
        book = list_in[idx]
        for inc in range(0, len(list_in)):
            book_comp = list_in[inc]
            book = list_in[idx]
            if book.title < book_comp.title:
                list_in[inc] = book
                list_in[idx] = book_comp

# Part 2
# Purpose: this function takes a string value and returns a string value where
#          all previously upper-cased letters are now lowercase and vice-versa.
# Input: str
# Output: str
# Example of Input: BaNaNa
# Example of Output: bAnAnA

def swap_case(str_in: str) -> str:
    comp_list = []
    for letter in range(len(str_in)):
        if str_in[letter].isalpha() and str_in[letter].isupper():
            comp_list.append(str_in[letter].lower())
        elif str_in[letter].isalpha() and str_in[letter].islower():
            comp_list.append(str_in[letter].upper())
        else:
            comp_list.append(str_in[letter])
    str_out = ''.join(comp_list)

    return str_out

# Part 3
# Purpose: this function takes in a string value, and two other string values representing
#          old and new respectively; returns a new string where each old value is replaced
#          with the new value.
# Input: str, str (single character), str (single character)
# Output: str
# Example of Input: "abcdcba", 'a', 'x'
# Example of Output: "xbcdcbx"

def str_translate(str_in: str, old_char: str, new_char: str) -> str:
    comp_list = []

    for letter in str_in:
        if letter == old_char or letter == old_char.upper():
            letter = new_char
        comp_list.append(letter)

    str_out = ''.join(comp_list)
    return str_out

# Part 4
# Purpose: this function takes a string value and returns a dictionary that maps
#          each "word" from the string as a count for the amount of times it
#          appears in the string.
# Input: str
# Output: dict[str: int]
# Example of Input: "This is how this works"
# Example of Output: {"This": 2, "is": 1, "how": 1, "works": 1}

def capitalize(word_in: str) -> str:
    letter_list = []
    letter_list.append(word_in[0].upper())
    for letter in range(1, len(word_in)):
        letter_list.append(word_in[letter])
    str_out = "".join(letter_list)
    return str_out

def remove_punc(word_in: str) -> str:
    if not word_in.isalpha():
       return word_in[:-1]
    return word_in

def histogram(str_in: str) -> dict[str, int]:
    words = {}
    case = {}
    inc = 0
    sentence = str_in.split(" ")
    for idx in range(len(sentence)):
        if sentence[idx].islower():
            sentence[idx] = capitalize(sentence[idx])
            sentence[idx] = remove_punc(sentence[idx])
        if sentence[idx] in words:
            inc = (words[sentence[idx]] + 1)
            case = {sentence[idx]: inc}
            words.update(case)
        elif sentence[idx] not in words:
            case = {sentence[idx]: 1}
            words.update(case)
    return words



