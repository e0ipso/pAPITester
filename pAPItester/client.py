import argparse
import json
from httplib import HTTPConnection, HTTPSConnection, HTTPException
import sys

def getArguments():
  parser = argparse.ArgumentParser()
  parser.add_argument('method', help='the HTTP verb to use', choices=['GET', 'POST', 'PUT'])
  parser.add_argument('route', help='the route where to make the request')
  parser.add_argument('--data', help='the data associated to the POST or PUT request')
  parser.add_argument('-c', '--config-file', help='file where to load settings from', default='./config/settings.json')
  return parser.parse_args()

class ApplicationException(Exception):
  """Custom exception for exception scoping."""

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

class ApplicationRequest(object):
  """Wrapper class around urllib2.Request to deal with the application data."""
  def __init__(self, settings):
    self.__settings = settings
    # Build the request url
    url = self.buildUrl()
    print settings['runtime']['method'] + ' ' + url
    # Create the self.connection property according to the values of the configuration.
    try:
      if (settings['host']['url']['protocol'] == 'https'):
        self.connection = HTTPSConnection(settings['host']['url']['hostname'], settings['host']['url']['port'], settings['network']['privateKeyFile'], settings['network']['certFile'], True, settings['network']['timeout'], settings['network']['sourceAddress'])
      else:
        self.connection = HTTPConnection(settings['host']['url']['hostname'], settings['host']['url']['port'], True, settings['network']['timeout'], settings['network']['sourceAddress'])
    except HTTPException as e:
      sys.stderr.write("HTTP Error. Closing connection.\n")
      raise ApplicationException(e.str())
    self.connection.set_debuglevel(settings['client']['verboseLevel'])

  def buildUrl(self):
    """Builds the URL from the settings object."""
    port = self.__settings['host']['url']['port'] if self.__settings['host']['url']['port'] else (443 if self.__settings['host']['url']['protocol'] == 'https' else 80)
    return self.__settings['host']['url']['protocol'] + '://' + self.__settings['host']['url']['hostname'] + ':' + str(port) + self.buildRoute()

  def buildRoute(self):
    return '/' + self.__settings['host']['url']['endpoint'].strip('/') + '/' + self.__settings['runtime']['route']

  def alterSettings(self, newSettings):
    """Replace the settings dict entirely by another one."""
    self.__settings = newSettings

  def request(self):
    """Make the request."""
    self.connection.request(self.__settings['runtime']['method'], self.buildRoute(), None, self.__settings['network']['headers'])
    return self.connection.getresponse()

  def __del__(self):
    """Close the connection before object destruction."""
    self.connection.close()
