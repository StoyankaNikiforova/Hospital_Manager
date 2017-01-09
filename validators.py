from functools import wraps


def pass_validate(num):
    def wraper(func):
        @wraps(func)
        def validator(*args, **kwargs):

            return
        return validator
    return wraper


def check_pass():
    def check_func(func):
        @wraps(func)
        def cheker(*args, **kwargs):
            return func(*args, **kwargs)
        return cheker
    return check_func
