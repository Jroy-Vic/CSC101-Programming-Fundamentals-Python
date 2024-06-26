import convert

# Roy Vicerra

# Task 2
# Purpose: this function does not take any imputs, however it will
#          return a list of float values; the function must read
#          a series of numbers from the user, though only one number
#          must be inputted at a time; the list ends when the user
#          inputs "done".
# Input: user_input(float)
# Output: list[float]
# Example Input: 1, 2, "hello", 4, 5, "done"
# Example Output: [1.0, 2.0, 4.0, 5.0]

def gather_numbers():
    list_out = []
    user = input("Input a number: ")

    while user != "done":
        data = convert.str_to_float(user)
        if data != None:
            list_out.append(data)
        user = input("Input a number: ")

    print(list_out)

if __name__ == '__main__':
    gather_numbers()


