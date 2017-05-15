#coding: utf-8
import optparse
import socket
from socket import *

def connScan(tgtHost,tgtPort):
    try:
        connSkt=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #套接字格式：
        #AF_UNIX:只能用于单一的Unix系统进程间通信
        #AF_INET:服务器之间网络通信
        #AF_INET:IPv6
        #SOCKET_STREAM:流式socket，for TCP
        #SOCK_DGRAM:数据报式socket，for UDP
        connSkt.connect((tgtHost,tgtPort))
        connSkt.send('ViolentPython\r\n')
        results=connSkt.recv(100)
        print '[+] %d/tcp open'% tgtPort
        print '[+]'+str(results)
        connSkt.close()
    except:
        print '[-]%d/tcp closed'% tgtPort

def portScan(tgtHost,tgtPorts):
    try:
        tgtIP=gethostbyname(tgtHost)
    except:
        print "[-] Cannot resolve '%s':Unknown host"%tgtHost
        return

    try:
        tgtName=gethostbyaddr(tgtIP)
        print '\n[+] Scan Results for :'+tgtName[0]
    except:
        print '\n[+] Scan Results for :'+tgtIP

    setdefaulttimeout(1)

    for tgtPort in tgtPorts:
        print 'Scanning port'+tgtPort
        connScan(tgtHost,int(tgtPort))

def main():
    parser = optparse.OptionParser('usage %prog -H' + '<target host> -p <target port>')
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-p', dest='tgtPort', type='string', help='specify target port[s] separated by comma')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')
    if (tgtHost == None) | (tgtPorts == None):
        print '[-] You must specify a target host and port[s].'
        exit(0)
    portScan(tgtHost,tgtPorts)

if __name__ == '__main__':
    main()


