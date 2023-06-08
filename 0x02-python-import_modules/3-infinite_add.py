#!/usr/bin/python3

if __name__ == "__main__":
    """Print the addition of all arguments."""
    import sys
    ttl = 0
    for x in range(len(sys.argv) - 1):
        ttl += int(sys.argv[x + 1])
    print("{}".format(ttl))
