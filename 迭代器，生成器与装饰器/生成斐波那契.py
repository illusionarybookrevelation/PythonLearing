import sys

def fibonacci(numbers):
    a,b,counter = 0,1,0
    while True:
        if counter > numbers:
            break
        yield a
        a,b = b,a+b
        counter += 1
f  = fibonacci(10)

while True:
    try:
        print(next(f),end=" ")
    except StopIteration:
        sys.exit()

