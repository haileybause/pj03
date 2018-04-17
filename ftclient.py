import threading
from socket import *
import argparse
import binascii
from struct import *

def parseArgs():
  """parses command line argument for client"""
  parser = argparse.ArgumentParser()
  #adds server argument
  parser.add_argument('--server')
  #mutually exclusive group to determine if in send or receive mode
  group = parser.add_mutually_exclusive_group()
  group.add_argument('--receive', action = 'store_true')
  group.add_argument('--send', action = 'store_true', nargs = '+')
  
  arg = parser.parse_args()
  server = arg.server
  receive = arg.receive
  send = arg.send
  #returns arguments
  return server, receive, send

#gets all command line arguments and sets to corresponding variables
server, receive, send = parseArgs()
if(send):
  ID = send[0]
  filename = send[1]
  
