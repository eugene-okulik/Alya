def finish_me(func):
    def wrapper():
        func()
        print('finished')

    return wrapper


@finish_me
def print_me():
    print('print me')


print_me()
