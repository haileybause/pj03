import threading
from socket import *
import argparse
import binascii
from struct import *

def parseArgs():
  """parses command line argument for client"""
  parser = argparse.ArgumentParser()
  #adds server argument                                                             
  parser.add_argument('--server', required=True)
  #mutually exclusive group to determine if in send or receive mode                 
  group = parser.add_mutually_exclusive_group()
  group.add_argument('--receive', action = 'store_true')
  group.add_argument('--send', nargs = '+')
  #adds other options                                                               
  parser.add_argument('-s', '--size')
  parser.add_argument('-p', '--port')
  parser.add_argument('-c', '--cons')
  arg = parser.parse_args()
  server = arg.server
  receive = arg.receive
  send = arg.send
  size = arg.size
  port = arg.port
  cnum = arg.cons
  #returns arguments                                                                
  return server, receive, send, size, port, cnum


print(parseArgs())
#gets all command line arguments and sets to corresponding variables                
server, receive, send, size, port, cnum = parseArgs()
if(send):
  ID = send[0]
  filename = send[1]

