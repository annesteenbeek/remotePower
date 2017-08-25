#!/usr/bin/env python

import logging
from logging.handlers import RotatingFileHandler, SysLogHandler
from flask import Flask
from wakeonlan import wol
import requests

MAC_ADDR = '68.05.CA.21.31.97'
NAS_IP = '192.168.2.12'
IP_TARG = '192.168.2.255'
FLASK_PORT = 5000
PASSWORD = #PASSWORD

app = Flask(__name__)

logHandler = SysLogHandler(address='/dev/log')
logHandler.setLevel(logging.INFO)
logger = logging.getLogger() # root logger
logger.addHandler(logHandler)
logger.setLevel(logging.INFO)
app.logger.addHandler(logHandler)
app.logger.setLevel(logging.INFO)

@app.route('/wakeserver')
def wakeserver():
    wol.send_magic_packet(MAC_ADDR, ip_address=IP_TARG)
    return 'Wake server successful'

@app.route('/shutdownserver')
def shutdown_server():
    try:
        r = requests.post(
             "http://"+NAS_IP+"/api/v1.0/system/shutdown/",
             auth=('root', PASSWORD))
        if r.text == "Shutdown process started.":
            rval = "Shutdown success\n"
        else:
            rval = r.text + "\n"
    except:
        rval = "Failed to shutdown server\n"
    finally:
        return rval

if __name__=='__main__':
	app.run(host='0.0.0.0',port=FLASK_PORT)
