def meta_decorador(variable):
    print('meta decorador {0}'.format(variable))

    def login(func):
        def auth(*args, **kwargs):
            print('args {0}'.format(args))
            print('kwargs {0}'.format(kwargs))
            return func(*args, **kwargs)

        return auth

    return login


@meta_decorador(200)
def test():
    print('hello')


if __name__ == '__main__':
    test()
