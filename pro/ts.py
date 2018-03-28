#!/usr/bin/env python
# encoding: utf-8
import sys,os,logging,re
import time
from socket import gethostname
from optparse import OptionParser
from logging.handlers import RotatingFileHandler
from prometheus_client import CollectorRegistry, Gauge, push_to_gateway

host = gethostname().split('.')[0]

PUSH_GATEWAY = "gateway.video.monitor.lecloud.com:9091"

parser = OptionParser()
parser.add_option("-f", "--logfile", action="store", type="string",
                  dest="logfile", help="the logfile")

(options, args) = parser.parse_args()

if not options.logfile:
    parser.exit(-1,parser.print_help())

if not os.path.exists(options.logfile):
    logging.error("logfile: [%s] do not exist..."%logfile)
    parser.exit(-1,parser.print_help())

LOG_FILE = '/tmp/live_logstatus_monitor.log'

#log config
Rthandler = RotatingFileHandler(LOG_FILE, maxBytes=10*1024*1024, backupCount=5)
Rthandler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
Rthandler.setFormatter(formatter)
logging.getLogger('').addHandler(Rthandler)

SEEK_STATS = None
FD = None

TIMESTRING = '%Y-%m-%d %H:%M:%S'


def pattern_check(pattern):
    try:
        pattern = re.compile(pattern)
        return patten
    except:
        logging.error("pattens: [%s] is error pl check"%pattern)
        return None

def handle_key(logfile, fd, **kw):
    global SEEK_STATS
    registry=kw.get('registry')

    p_push = re.compile(r'Time:(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}),\s+.*Stream:(.*),\s+PushRate:(.*),\s')
    p_pull = re.compile(r'Time:(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}),\s+.*Stream:(.*),\s+ClientIP:(\d+\.\d+\.\d+\.\d+)_(\d+),.*DistributeR
ate:(.*),\s')

    file_size = os.path.getsize(logfile)

    if not SEEK_STATS:
        SEEK_STATS = file_size

    file_seek = SEEK_STATS

    SEEK_STATS = file_size

    if file_size > 0:

        if file_size < file_seek:
            file_seek = 0

        fd.seek(file_seek, 0)
        content = fd.read()

        _tmp_push_rate = re.findall(p_push, content)
        _tmp_pull_rate = re.findall(p_pull, content)

        push_data = kw.get('push')
        pull_data = kw.get('pull')

        for push_content in _tmp_push_rate:
            stream = push_content[1]
            pushrate = push_content[2]

            push_data.labels(stream=stream, instance=host).set(pushrate)

        for pull_content in _tmp_pull_rate:
            stream = pull_content[1]
            clientip = pull_content[2]
            clientport = pull_content[3]
            pullrate = pull_content[-1]

            pull_data.labels(stream=stream, instance=host, clientip=clientip, clientport=clientport).set(pullrate)

        push_to_gateway('gateway.video.monitor.lecloud.com:9091', job="live-rtmpstream-status", registry=registry)


def main():
    fd = open(options.logfile)
    registry = CollectorRegistry()
    push_metric = "live_rtmp_push_rates"
    push_data = Gauge(push_metric, 'Live Rtmp Push Stream Rates', \
                  labelnames=('instance', 'stream'), registry=registry)
    pull_metric = "live_rtmp_pull_rates"
    pull_data = Gauge(pull_metric, "Live Rtmp Pull Stream Status", \
		labelnames=('instance', 'stream', 'clientip', 'clientport'), registry=registry)

    while True:
        time.sleep(10)
        handle_key(options.logfile, fd, registry=registry, push=push_data, pull=pull_data)

if __name__ == '__main__':
    main()