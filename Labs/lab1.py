import random

N = 10
demo_array = [[random.random() for i in range(N)] for j in range(N)]

def factorial(n):
    result = 1
    for x in range(1, n):
        result = result * x
        print result
    return result


demo_factorial = factorial(10)
print demo_factorial

array_string = ','.join(str(v) for v in demo_array)

f = open("demo.txt", "w")
f.write(array_string)
f.close()
f = open("demo.txt", "r")
print(f.read())
