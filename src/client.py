#!/usr/bin/python

import argparse

def getArguments():
  parser = argparse.ArgumentParser()
  parser.add_argument('method', help='the HTTP verb to use', choices=['GET', 'POST', 'PUT'])
  parser.add_argument('route', help='the route where to make the request')
  parser.add_argument('--data', help='the data associated to the POST or PUT request')
  parser.add_argument('-c', '--config-file', help='file where to load settings from', default='./config/settings.json')
  return parser.parse_args()
