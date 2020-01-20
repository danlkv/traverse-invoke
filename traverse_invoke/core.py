import pprint as pp
from loguru import logger as log
import sys
log.remove()
log.add(sys.stdout, level='INFO')
pprint = pp.pprint
from traverse_invoke.leaves import kwarg
leaf = kwarg

def entry_descent(config, path, funcs, leaf=leaf):
    log.info(f'Config: {pp.pformat(config)}')
    log.info(f'Path {path}')
    descent(config, path, funcs, leaf=leaf)

def entry_traverse(config, path, funcs, leaf=leaf):
    log.info(f'Config: {pp.pformat(config)}')
    log.info(f'Path {path}')
    traverse(config, path, funcs, leaf=leaf)


# One way
def descent(config, path, funcs, leaf=leaf):
    log.info(f'Current path: {path}')
    fname = path.pop(0)
    config.update(config.get(fname, {}))
    f = funcs.get(fname)
    if isinstance(f, dict):
        funcs.update(f)
        descent(config, path, funcs)

    config[fname] = '<<Entered deleted>>'
    del config[fname]
    leaf(funcs[fname], config)
    if len(path):
        descent(config, path, funcs)

def node(fname, funcs, config, leaf=leaf):
    f = funcs.get(fname)
    if isinstance(f, dict):
        return funcs[fname]
    else:
        leaf(f, config)
        if f  is None:
            return None
        return funcs

def node2(fname, funcs, config, leaf=leaf):
    f = funcs.get(fname)
    if isinstance(f, dict):
        return funcs[fname]
    else:
        if f  is None:
            config[fname] = TypeError()
        return funcs

## Another way
def traverse(config, path, funcs, leaf=leaf):
    while len(path) > 0:
        this_config = config.copy()
        this_funcs = funcs.copy()

        log.info(f'Current path: {path}')
        fname = path[0]
        this_config.update(config.get(fname, {}))

        f = node2(fname, this_funcs, this_config, leaf=leaf)
        turn = leaf(this_funcs.get(fname), this_config)
        print(2,f)
        if turn: break
        path.pop(0)
        traverse(this_config, path, f, leaf=leaf)

        log.info(f'Renurned traverse, path: {path}')


