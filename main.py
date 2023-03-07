def mygenerator():
    yield 1
    yield 2
    yield 3


gen = mygenerator()
print(sum(gen))
print(sorted(gen))

def countdown(num):
    print("Starting")
    while num > 0:
        yield num
        num -= 1


cd = countdown(4)
print(next(cd))
for i in cd:
    print(i)


def first(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums


print(sum(first(46)))


# Generating such a number:
def first_generator(first_num):
    num = 0
    while num < first_num:
        yield num
        num += 1


print(list(first_generator(46)))


def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


fib = fibonacci(30)
for i in fib:
    print(i)
generator = (i for i in range(10) if i % 2 == 0)
for i in generator:
    print(i)
generator = [i for i in range(10) if i % 2 == 0]
print(generator)
