def reduct(func, config):
    try:
        r = func(**config)
        if r is not None:
            config[func.__name__] = r
        else:
            return True
    except Exception as e:
        try:
            config[func.__name__] = e
        except:
            print('func is', func)
        print("error:", e)

