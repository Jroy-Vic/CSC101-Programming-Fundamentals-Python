# Roy Vicerra

# Task 1
# Purpose: this function takes a single str value input and returns
#          an Optional[float]; if the input is a float value, it will
#          be converted into a float value and return it; if not possible,
#          return None.
# Input: str
# Output: Optional[float]
# Example Input:
# Example Output:

def str_to_float(value: str) -> float:
   try:
       float_value = float(value)
       return float_value
   except ValueError:
       return None

