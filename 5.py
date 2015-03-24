import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--speaker', nargs=2)
parser.add_argument('--visitors', type=int)
parser.add_argument('-a', '--attendee', dest="attendees", nargs='*')
args = parser.parse_args()

print (args.attendees)
