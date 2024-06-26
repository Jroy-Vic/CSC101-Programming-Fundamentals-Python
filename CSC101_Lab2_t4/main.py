# Roy Vicerra - Lab 2 Task 4

from typing import Optional

def checked_access(L:list[int],idx:int) -> Optional[int]:
    test = idx >= 0 and idx < len(L)  # first: the value of test comes out as False
                                      # second: the value of test comes out as True
    if test:  # This check is preventing any calls that produces a False value of test to be returned
        return L[idx]
    else:
        return None

first = checked_access([1,0,1],9)  # first = None
second = checked_access([1,0,1],2)  # second = 1
print(second)

# ~~~~~~

# Roy Vicerra - Lab 2 Task 4
def length_sum(L:list[str]) -> int:
    if len(L) > 2:
        result = len(L[0]) + len(L[1]) + len(L[2])  # the statement is evaluated by the call first
                                                    # the values being added are: 4 + 2 + 3
    elif len(L) > 1:
        result = len(L[0]) + len(L[1])  # the statement is evaluated by the call third
                                        # the values being added are: 7 + 4
    elif len(L) > 0:
        result = len(L[0])  # the statement is evaluated by the call second
                            # the values being added are: 11
    else:
        result = 0
        return result

first = length_sum(["this","is","the","first","call"])
second = length_sum(["second call"])
third = length_sum(["another","call"])
print(third)

# ~~~~~

# Roy Vicerra - Lab 2 Task 4
def surprising(L:list[str], other:str) -> list[str]:
    L.append(other.upper())
    return L

words = ["this","is","confusing","code."]
first = surprising(words, "Avoid")
second = surprising(words, "such.")
         # the value of words at this point is: 5 (6 items in total) -> ["this","is","confusing","code","Avoid","such."]
         # the values of first at this point is: 5 (6 items in total) -> ["this","is","confusing","code","Avoid","such."]
         # the values of second at this point is: 5 (6 items in total) -> ["this","is","confusing","code","Avoid","such."]
         # Because lists are a mutable item, when calling second it will change...
         # ...the original list L even when calling first afterwards
print(second)