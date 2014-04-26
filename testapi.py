import pAPItester.client
import json

def main():
  args = pAPItester.client.getArguments()
  try:
    json_string = open(args.config_file).read()
    parsed_object = json.loads(json_string)
    print parsed_object
  except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)

if __name__ == '__main__':
  main()
