def decorated(arg):
    print("Decorator applied with argument " + arg)

    def wrapper(func):
        print("Wrapper created for decorator for function " + func.__name__)

        def decorator(arg):
            return "<dec>" + func(arg) + "</dec>"

        return decorator

    return wrapper


@decorated("argumentet")
def test(arg):
    return "Dette er test-funksjonen med argument " + arg


print(test("Magnus"))


def test2(test, *args, **kwargs):
    print("args: {}".format(args))
    print("kwargs: {}".format(kwargs))


test2("Nei", 2, hei="Ja", test="Haja")
