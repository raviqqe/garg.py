import gargparse


gargparse.add_argument("-f", "--foo",
                       type=str, default="bar",
                       help="This is an example.")
print(gargparse.ARGS.foo)
