# Your code here
def list_and_tuple(*args):
    lst = list(str(x) for x in args)
    tpl = tuple(str(x) for x in args)

    return lst ,tpl

