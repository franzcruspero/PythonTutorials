from functools import wraps

def ensure_no_kwargs(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs:
            raise ValueError("No kwargs allowed! Sorry :(")
        return fn(*args, **kwargs)
    return wrapper

def ensure_first_arg_is(val):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if args and args[0] != val:
                return f"First arg needs to be {val}!"
            return fn(*args, **kwargs)
        return wrapper
    return inner

# enforcing data types as arguments
def enforce(*types):
    def decorator(f):
        def new_func(*args, **kwargs):
            newargs = []
            for (a, t) in zip(args, types):
                newargs.append( t(a))
            return f(*newargs, **kwargs)
        return new_func
    return decorator

@ensure_first_arg_is("burrito")
def fav_food(*args):
    print(args)


@ensure_no_kwargs
def greet(name):
    print(f"Hi there {name}")

@enforce(str, int)
def repeat_msg(msg, times):
    for time in range(times):
        print(msg)

@enforce(float, float)
def divide(a,b):
    print(a/b)


repeat_msg("hello", '3')
divide('1','2')
# fav_food('burrito', 'lumpia')
# print(fav_food('pork chop', 'lumpia'))