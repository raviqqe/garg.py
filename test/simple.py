import gargparse


gargparse.add_argument('foo', type=str, help="This is an example.")
gargparse.parse_args(['bar'])
print(gargparse.ARGS.foo)
