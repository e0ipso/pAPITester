import pAPItester.client
import pAPItester.util
import json

def main():
  args = pAPItester.client.getArguments()
  logger = pAPItester.util.TerminalLogger(2)
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
    logger.log(response.read(), logger.ok)

  except IOError as e:
    msg = "I/O error({0}): {1}".format(e.errno, e.strerror)
    logger.log(msg, logger.error)

if __name__ == '__main__':
  main()
