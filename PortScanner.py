#!/usr/bin/python3

# Import the necessary libraries
import optparse  # For parsing command-line options
from socket import *  # For socket programming 
from threading import *  # For multi-threading support
from termcolor import colored  # For colored terminal output

# Function to attempt a connection to a specified IP and port
# On success, outputs in green indicating the port is open
# On failure, outputs in red indicating the port is closed
def connectScan(trtIP, trtPort):
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((trtIP, trtPort))
        print(colored('[+] %d / TCP open' % trtPort, 'green'))
    except:
        print(colored('[-] %d / TCP closed' % trtPort, 'red'))
    finally:
        sock.close()

# Function to initiate a port scan on the target host
# Resolves the host name to an IP address
# Sets a default timeout for socket connections
# Uses multi-threading to scan multiple ports concurrently
def startPort(trtHost, trtPorts):
    try:
        trtIP = gethostbyname(trtHost)
    except:
        print('Unknown Host %s' % trtHost)
        return

    try:
        trtNme = gethostbyaddr(trtIP)
        print('Scan result for %s' % trtNme[0])
    except:
        print('Scan result for %s' % trtIP)

    setdefaulttimeout(1)
    for trtPort in trtPorts:
        thr = Thread(target=connectScan, args=(trtIP, int(trtPort)))
        thr.start()

# Function to parse command-line arguments and initiate the port scan
# -t flag for target host (IP or hostname)
# -p flag for target ports (comma-separated list)
def startParser():
    parser = optparse.OptionParser('[*] Usage of the script: ' + '-t <target ip or name> -p <target port(s)>')
    parser.add_option('-t', dest='trtHost', type='string', help='specify target host')
    parser.add_option('-p', dest='trtPort', type='string', help='specify target ports separated by commas')
    (options, args) = parser.parse_args()
    
    trtHost = options.trtHost
    trtPorts = str(options.trtPort).split(',')
    
    if trtHost is None or trtPorts[0] is None:
        print(parser.usage)
        exit(0)
    
    startPort(trtHost, trtPorts)

# Main function to start the parser
startParser()


