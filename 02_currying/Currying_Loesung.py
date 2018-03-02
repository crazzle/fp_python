def curry(func):
    """Truly curry a function of any number of parameters
    returns a function with exactly one parameter
    When this new function is called, it will usually create
    and return another function that accepts an additional parameter,
    unless the original function actually obtained all it needed
    at which point it just calls the function and returns its result
    """
    def curried(*args):
        """
        either calls a function with all its arguments,
        or returns another functiont that obtains another argument
        """
        if len(args) == func.__code__.co_argcount:
            ans = func(*args)
            return ans
        else:
            return lambda x: curried(*(args+(x,)))

    return curried