# def foo():
#     if not hasattr(foo, 'counter'):
#         foo.counter = 0
#     foo.counter += 1
#     print(foo.counter)
#     return 'None'
#
# print(foo())
# print(foo())
# print(foo())







def counter(func):
    COUNTER = 0
    def wrapper():
        # print('BEFORE')
        nonlocal COUNTER
        COUNTER += 1
        print(COUNTER)
        result = func()
        # print(f'RESULT: {result}')
        # print('AFTER')
        return result

    return wrapper


@counter
def foo():
    return "None"

# foo = counter(foo)
foo()
foo()
foo()
