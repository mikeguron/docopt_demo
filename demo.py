# author: Tiffany Timbers
# date: 2020-01-15

"""This script prints out docopt args.
Usage: demo.py <arg1> --arg2=<arg2> [--arg3=<arg3>]

Options:
<arg1>             Takes any value (this is a required positional argument)
--arg2=<arg2>     Takes any value (this is a required option)
[--arg3=<arg3>]   Takes any value (this is an optional option)
[<arg_new>]       Takes any value (this is an optional positional argument)
""" 

from docopt import docopt
opt = docopt(__doc__)

def main(arg1, arg2, arg3, arg_new):
  print(opt)
  print(type(opt))

if __name__ == "__main__":
    main(opt["arg1"], opt["--arg2"], opt["--arg3"], opt["arg_new"])
    
