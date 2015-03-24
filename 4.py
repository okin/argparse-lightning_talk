import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--location', default="CCC FFM HQ")
parser.add_argument('--no-ug', action="store_false", help="Disable usergroup.")
parser.add_argument('-a', '--attendee', dest="attendees", action="append")
args = parser.parse_args()

print (args.attendees)
