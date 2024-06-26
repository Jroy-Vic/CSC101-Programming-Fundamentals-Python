# Roy Vicerra - Lab3 Task1

more = [x + 1 for x in [1,2,3,4]]  # the values of x at each step: 1, 2, 3, 4
print(more)  # more = [2,3,4,5]

# ~~~~~~

# Roy Vicerra - Lab3 Task1

def square(n:int) -> int:
    return n * n   # square(1) => n=1, return 1
                   # square(2) => n=2, return 4
                   # square(3) => n=3, return 9
                   # square(4) => n=4, return 16

squares = [square(x) for x in [1,2,3,4]]  # squares = [1,4,9,16]
print(squares)  # This relates to the values recorded above because they are the squares of the values (i.e. 2^2 = 4)

# ~~~~~~

# Roy Vicerra - Lab3 Task1

def check(n:int) -> bool:
    return n > 2  # check(0) => n=0, return False
                  # check(1) => n=1, return False
                  # check(2) => n=2, return False
                  # check(3) => n=3, return True
                  # check(4) => n=4, return True

answer = [x for x in range(5) if check(x)]  # answer = [3,4]
print(answer)

# ~~~~~~

# Roy Vicerra - Lab3 Task1

def inc(m:int) -> int:
    return m + 1  # inc(0) => m=0, return 1
                  # inc(1) => m=1, return 2
                  # inc(2) => m=2, return 3
                  # inc(3) => m=3, return 4
                  # inc (4) => m=4, return 5

def check(n:int) -> bool:
    return n > 2  # check(0) => n=0, False
                  # check(1) => n=1, False
                  # check(2) => n=2, False
                  # check(3) => n=3, True
                  # check(4) => n=4, True

answer = [inc(x) for x in range(5) if check(x)]  # answer = [4,5]
print(answer)