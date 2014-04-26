This repo contains the code for the first iteration of the Continuous Hackathon.

## Project description.
This is a python based command line utility that will allow you to test the output of an API under from the command line.

This is not intended to be more than a refresh of the python syntax and some playing.

## Usage
To get help on the app usage execute it without any arguments.

```sh
python testapi.py
```

You will need a configuration file in the `config` folder. Copy
`default-settings.json` to another file and adjust the settings accordingly.

## Configuration file
`config/default-settings.json` is the default configuration file. This file is not used, it is here
only for documentation purposes. Copy this to be settings.json and the app
will use it as a default if no other confiruation is specified. You can have
as many configuration files as you need, specify the configuration file to
load with the command line options.

  * `host`: Information about the remote host.
    * `url`:
      * `protocol`: Protocol used when building the URL for the call.
      * `hostname`: Host name used when building the URL for the call.
      * `endpoint`: Endpoint used when building the URL for the call. Used for scoping purposes.
      * `port`: Leave it at null to use the default port depending on the selected protocol. 80 for http and 443 for https.
    * `authentication`: How to authenticate requests to the server.
      * `type`: Supported: none, oauth, basic.
      * `settings`: Custom settings to be read.
  * `client`: Configuration about how the client app should behave.
    * `verboseLevel`: Output format when displaying info in the screen. Only supports json. 0: silent, 1: log, 2: chatty
    * `outputFormat`: Currently only json is supported.
  * `network`:
    * `headers`: Custom headers to be sent with the request.