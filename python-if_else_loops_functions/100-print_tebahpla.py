#!/usr/bin/python3

print("".join("{:c}".format(c - (32 * (c % 2))) for c in range(122, 96, -1)),
      end="")
