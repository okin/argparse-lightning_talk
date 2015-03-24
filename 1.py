import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-s', help='a short option')
parser.add_argument('--long-opt', help='a long option')
parser.add_argument('-b', '--both', help='both')
parser.add_argument('-t', '--tri', '-3', help='and more!')

args = parser.parse_args()
