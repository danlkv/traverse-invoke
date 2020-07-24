def kwarg(func, config):
    if func is None:
        return True
    if isinstance(func, dict):
        return
    if hasattr(func, '__call__'):
        func(**config)
    else:
        raise Exception(f'trying to call {func}')
