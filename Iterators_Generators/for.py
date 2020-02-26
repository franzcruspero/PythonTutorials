def my_for(iterable, func):
    iterator = iter(iterable)
    while iterator:
        try:
            thing = next(iterator)
        except StopIteration:
            break
        else:
            func(thing)

def square(x):
    print(x*x)

my_for("hello", print)
my_for([1,2,3,4], square)