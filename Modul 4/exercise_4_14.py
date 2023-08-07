import sys


def parse_args():
    result = ""
    for i in range(1, len(sys.argv)):
        if i == len(sys.argv):
            result += sys.argv[i]
        else:
            result += sys.argv[i] + ' '

    return result

print(parse_args())
print(sys.argv)
