# Roy Vicerra - Lab 1 Task 5

def function1(x,y):
    z=x+y*2
    return z+4

result=function1(2*2,4-1)
print(result)

# When prompted by the IDE, step into the call that must be evaluated first.
def square(n:float) -> float:
    return n * n                 # the value first returned by square is 4. n is 2.


result = square(square(2))       # the value of result is 14.
print(result)

def function2(a:int, b:int) -> int:
    c = a + b                    # a and b are related before the call, they are declared as integers.
    return c**2                  # the value returned is 16.

a = 9
b = 7
answer = function2(b, a)         # the value of answer is 256.
print(c)                         # c is not defined because it is not a global variable.