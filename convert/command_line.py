import sys
import convert

# Roy Vicerra

# Task 3

def main():
    total = 0
    user = sys.argv
    for input in user:
        input_float = convert.str_to_float(input)
        if input_float != None:
            total = total + input_float
    return total

if __name__ == '__main__':
    print(sys.argv)
    print(main())