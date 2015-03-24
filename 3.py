import argparse

parser = argparse.ArgumentParser(prog="program name",
                                 description="Doing amazing things!",
                                 epilog="Still amazing after the help.",
                                 prefix_chars='*')
parser.add_argument('**thingy')
args = parser.parse_args()

print (args.thingy)
