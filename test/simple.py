import gargparse


gargparse.add_argument('foo', type=str, help="This is an example.")
args = gargparse.parse_args(['bar'])
print(args.foo)
