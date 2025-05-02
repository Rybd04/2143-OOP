def MyKwargs(argv):
    args = []
    kargs = {}

    for arg in argv:
        if ":" in arg:
            key, val = arg.split(":")
            kargs[key] = val
        else:
            args.append(arg.strip("-"))
    return args, kargs