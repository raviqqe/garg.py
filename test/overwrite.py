import gargparse


gargparse.add_argument("foo", type=str, help="This is an example.")
print(gargparse.ARGS.foo)
gargparse.parse_args(["bar"])
print(gargparse.ARGS.foo)
