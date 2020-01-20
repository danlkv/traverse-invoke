import inspect
from traverse_invoke.leaves import kwarg

def get_args(func, **kw):
    params = [ name for
        name, param in inspect.signature(func).parameters.items()
              if param.kind not in [param.VAR_POSITIONAL, param.VAR_KEYWORD]
    ]
    return params

def filter_dict(config, params, **kw):
    return {
        key : config.get(key) for
        key in params if config.get(key) is not None
    }

def adapt(func, config):
    config = filter_dict(config, get_args(func))
    return kwarg(func, config)

