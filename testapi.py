#!/usr/bin/python

import src.client
import json
import re

def main():
  args = src.client.getArguments()
  try:
    json_data = open(args.config_file).read()
    print json.loads(json_data)
  except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)

if __name__ == '__main__':
  main()
