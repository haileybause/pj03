import threading
from socket import *
import argparse
import binascii
from struct import *

def parseArg():
  """parses command line argument for server"""
  parser = argparse.ArgumentParser()
  parser.add_argument('-p', '--port')
  arg = parser.parse_args()
  port = arg.port
  #returns argument                                                                 
  return port

#sets server host and port                                                          
SEVER_HOST = '0.0.0.0'
SERVER_PORT = 47608
#if port is specified in command line, set it to server port                        
port = parseArg()
if(port):
  SERVER_PORT = port
SERVER_ADDR = (SERVER_HOST, SERVER_PORT)

class HandlerThread(threading.Thread):
  """handles threading for concurrent connections"""

  def __init(self, client, address):
    """constructor"""
    threading.Thread.__init__(self)
    self.client = client
    self.address = address

  def run(self):
    """thread code"""



connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
connection.bind(SERVER_ADDR)
connection.listen(10)

while True:
  client, address = connection.accept()
  th = HandlerThread(client, address)
  th.start()
