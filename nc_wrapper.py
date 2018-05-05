#!/usr/bin/python
import os
from subprocess import check_call
from subprocess import call

if __name__ == "__main__":
    message = '[sys="ZABRABET" env="TEST" org="zabbix" loc.inst="vm19485426-zabbix-srv" loc.inst="vm19485426-zabbix-srv" alarm.name="Lack of free swap space on vm19485426-zabbix-srv" alarm.state="red" time="2018-04-23T19:11:47+0000" msg="Free swap space in % (vm19485426-zabbix-srv:system.swap.size[,pfree]): 0%"]'

#    ip = '172.18.160.10'
#    port = '6514' #int(sys.argv[2])
    ip = '127.0.0.1'
    port = '7650'

    cmd = "echo '%s' | nc %s %s" % (message, ip, port)

    call(cmd, shell=True )
    #    c = call(lst_call, shell=False)


