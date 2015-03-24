import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--chaos', choices=['CHAOS', 'nope'])
parser.add_argument('--destroy', action="store_true", required=True)
args = parser.parse_args()

print (args.attendees)
