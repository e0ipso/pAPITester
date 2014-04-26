import argparse
import json
from urllib2 import Request

def getArguments():
  parser = argparse.ArgumentParser()
  parser.add_argument('method', help='the HTTP verb to use', choices=['GET', 'POST', 'PUT'])
  parser.add_argument('route', help='the route where to make the request')
  parser.add_argument('--data', help='the data associated to the POST or PUT request')
  parser.add_argument('-c', '--config-file', help='file where to load settings from', default='./config/settings.json')
  return parser.parse_args()

class ApplicationResponse(object):
  """Contains the response from the API server and the methods to handle them"""
  def str():
    """Convert the ApplicationResponse object into a printable string."""
    # This method gets magically invoked to print the object.
    print json.dumps(self.data, sort_keys = True,
                     indent = 2, separators = (',', ': '))

  def __init__(self, data):
    """Constructor method."""
    self.data = data

  def __iter__(self):
    """Tell the class how to be iterated."""
    return self.data

class ApplicationRequest(Request):
  def __init__(self, settings):
    self.__settings = settings
    # Call the Response constructor with the options we got from out settings.
    super(ApplicationRequest, self).__init__(url, data, headers, origin_req_host)
