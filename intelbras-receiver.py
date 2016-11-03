#!/usr/bin/env python
#
# Intelbras Router estatistcs receiver

import os
import signal
import time
import sys
import curses
import urllib2

dirpath = os.path.join(os.path.dirname(__file__), 'pylib')
if dirpath not in sys.path:
    sys.path.append(dirpath)

from tabulate import tabulate

header = {
    'Pragma': 'no-cache',
    'Origin': 'http://10.0.0.1',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'pt-BR,pt;q=0.8,en-US;q=0.6,en;q=0.4,hu;q=0.2',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.47 Safari/537.36',
    'Content-Type': 'text/plain;charset=UTF-8',
    'Accept': '*/*',
    'Cache-Control': 'no-cache',
    'Referer': 'http://10.0.0.1/sys_iptAccount.asp',
    'Cookie': 'admin:language=pt',
    'Connection': 'keep-alive',
    'DNT': '1'
}
request = urllib2.Request(
    'http://10.0.0.1/goform/updateIptAccount', headers=header)


def checkNetwork():
    u = urllib2.urlopen(request)
    out = u.read()
    u.close()

    currentIps = out.split('\n')
    lines = [["Source", "Down Kb/s", "Up Kb/s"]]
    for ipLine in currentIps:
        if ipLine is "":
            continue
        ipData = ipLine.split(';')
        ipData[2] = ipData[2] if float(
            ipData[2]) == 0.00 else '{0:8}'.format(ipData[2])
        ipData[1] = ipData[1] if float(
            ipData[1]) == 0.00 else '{0:8}'.format(ipData[1])
        lines.append([ipData[0], ipData[2], ipData[1]])

    return tabulate(lines, headers="firstrow")


def signal_handler(signal, frame):
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


def main(stdscr):
    sec = float(sys.argv[1]) if len(sys.argv) > 1 else 5
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    stdscr.addstr(0, 0, checkNetwork())
    stdscr.refresh()

    while True:
        stdscr.addstr(0, 0, checkNetwork())
        my, mx = stdscr.getmaxyx()
        stdscr.refresh()
        time.sleep(sec)


curses.wrapper(main)
