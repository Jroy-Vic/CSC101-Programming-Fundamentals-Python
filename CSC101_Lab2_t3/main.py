# Roy Vicerra - Lab 2 Task 3
def smallest(n:float, m:float) -> float:
    if n < m:
        return n  # this statement is not evaluated by any calls
    else:
        return m

first = smallest(3,2)  # the value of first is 2
second = smallest(2,2)  # the value of second is 2
                        # this is reasonable because 2 is not less than 2
print(second)

def function2(a:int, b:int, c:int) -> int:
    if a>b and a>c:
        return a-b  # this function is evaluated when a>b and a>c

    elif b>c:
        return b+c  # this function is evaluated when a<=b and a<=c and b>c

    else:
        return 2*c  # this function is evaluated when a<=b and a<=c and b<=c

answer1 = function2(3,2,1)  # answer1 = 1
answer2 = function2(2,3,1)  # answer2 = 4
answer3 = function2(2,1,3)  # answer3 = 6
print(answer3)