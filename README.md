# pj03
Hailey Bause (811967640)
Maja Culum ()

Description:
For this project we have implemented a concurrent server and client for a 
peer-to-peer text file transfer protocol over TCP. It can facilitate parallel 
and concurrent file transfers with user-specified buffer sizes.

To enter a cluster:
$ ssh vcf[number]

To activate virtual environment (from pj03 directory):
$ source bin/activate

To run server:
$ python3 ftserver.py [--port PORT]

To run client in receive mode:
$ python3 ftclient.py --server HOST:PORT [-s SIZE] [-p PORT] --receive

To run client in send mode:
$ python3 ftclient.py --server HOST:PORT [-c CNUM] [-s SIZE] --send ID FILE
