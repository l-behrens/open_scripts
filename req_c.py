#!/usr/bin/python
import logging
import socket
from logging import handlers
import sys

# Loglvl for netcool requests
NETCOOL_LVL = 60
LOG_FORMAT = 'zabbix.monitoring.test root: %(message)s'
logging.basicConfig(format = LOG_FORMAT)

def req_assembly(**args):

    for arg in args:
        ## manipulate query
        print(arg)
    return ""

if __name__ == "__main__":

    HOST = str(sys.argv[1])
    PORT = int(sys.argv[2])

    # Netcool call 

    message = '[sys="ZABRABET" env="TEST" org="zabbix" loc.inst="vm19485426-zabbix-srv" loc.inst="vm19485426-zabbix-srv" alarm.name="Lack of free swap space on vm19485426-zabbix-srv" alarm.state="red" time="2018-04-23T19:11:47+0000" msg="Free swap space in % (vm19485426-zabbix-srv:system.swap.size[,pfree]): 0%"]'

    # assign namespace
    logger = logging.getLogger('meyit.zappix.netcool')

    # 50 is highest conventional log lvl. Thats why this will not collide
    logger.setLevel(NETCOOL_LVL)

    address = (HOST, PORT)
    socktype = socket.SOCK_STREAM

    # create tcp syslog handler
    handler = handlers.SysLogHandler(address=address, socktype=socktype)
    handler.setFormatter(logging.Formatter(LOG_FORMAT))
    logger.addHandler(handler)

    # generate call
    msg = req_assembly(args = {'asdf':'asdf'})
    logger.log(NETCOOL_LVL, message)

    # clean up
    logger.removeHandler(handler)
