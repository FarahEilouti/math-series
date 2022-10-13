# user enter 0 ==> output is 0 //// user enter 1 ==> output is 1 //// user enter >1 ==> output fib 1 + fib 0,,,, 5= fib 4 + fib 3 
def fibonacci(n):
    """
    docs string 

    we create three functions of fibonacci, lucas and sum series

    in which we write the condition of each series rule to ensure the outpt result correctly by using pytest. 
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        return fibonacci(n-1) + fibonacci(n-2)

#print(fibonacci(7))        

def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    elif n > 1:
        return lucas(n-1) + lucas(n-2)  

#print(lucas(7))

def sum_series(n, first = 0, second = 1):
    if n == 0:
        return first
    elif n == 1:
        return second
    elif n > 1:
        # to remove default vals of first and second
        return sum_series(n-1, first, second) + sum_series(n-2, first, second)  

#print(sum_series(7,2,1))