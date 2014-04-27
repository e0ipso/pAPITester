import pAPItester.client
import json

def main():
  args = pAPItester.client.getArguments()
  try:
    json_string = open(args.config_file).read()
    conf = json.loads(json_string)
    conf['runtime'] = {
      'route': args.route,
      'method': args.method,
      'data': args.data
    }
    cli = pAPItester.client.ApplicationRequest(conf)
    response = cli.request()
    print str(response.status) + ' ' + response.reason
    print response.read()

  except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)

if __name__ == '__main__':
  main()
