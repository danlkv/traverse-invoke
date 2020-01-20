"""
This is demonstrative implementation of how to use
`traverse invoke` for implementation of its parts
"""
from .core import entry_traverse
from .adapt import get_args, filter_dict
from traverse_invoke.leaves import kwarg

# ## ## ## ## ## This is demonstrative stuff ######

def wrap(retkey):
    """
    This decorator writes output of decorated function
    to config variable ``retkey``

    :param retkey: key to store function return value
    :return: function
    """

    def wrap1(f):
        def wrapped(**config):
            ret = f(**config['this'])
            config['this'][retkey] = ret
        wrapped.__name__ = f.__name__
        wrapped.__doc__ = f.__doc__
        return wrapped
    return wrap1

funcs = {}
def fadd(f):
    funcs[f.__name__] = f
    return f

fadd(wrap('params')(get_args))
fadd(wrap('config')(filter_dict))

@fadd
@wrap(None)
def _wrap(func, config, **kw):
    print('$$\n$$\n this:', func, config)
    kwarg(func, config)

def adapt(func, config):
    entry_traverse(
        {'this':{'func':func, 'config':config}},

        '_get_args._filter_dict._wrap'.split('.'),

        funcs
        ,leaf=kwarg
    )
