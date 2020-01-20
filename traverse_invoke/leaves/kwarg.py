def kwarg(func, config):
    if func is None:
        return True
    if hasattr(func, '__call__'):
        func(**config)
    else:
        print('err')
        return
        raise Exception(f'trying to call {func}')
