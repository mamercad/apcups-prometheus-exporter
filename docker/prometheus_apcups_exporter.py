#!/usr/bin/env python3

import os
from datetime import datetime
import logging
import time

# import requests
import subprocess
from prometheus_client import start_http_server, Gauge


class APCUPS:
    def __init__(self):
        self.APC = None
        self.DATE = None
        self.HOSTNAME = None
        self.VERSION = None
        self.UPSNAME = None

        self.gauge_status = Gauge(
            name="apcups_status",
            documentation="UPS status. One or more of the following (space-separated): CAL TRIM BOOST ONLINE ONBATT OVERLOAD LOWBATT REPLACEBATT NOBATT SLAVE SLAVEDOWN or COMMLOST or SHUTTING DOWN",
        )
        self.gauge_linev = Gauge(
            name="apcups_linev", documentation="Current input line voltage"
        )
        self.gauge_loadpct = Gauge(
            name="apcups_loadpct",
            documentation="Percentage of UPS load capacity used as estimated by UPS",
        )
        self.gauge_bcharge = Gauge(
            name="apcups_bcharge",
            documentation="Current battery capacity charge percentage",
        )
        self.gauge_timeleft = Gauge(
            name="apcups_timeleft",
            documentation="Remaining runtime left on battery as estimated by the UPS",
        )
        self.gauge_mbattchg = Gauge(
            name="apcups_mbattchg",
            documentation="Min battery charge % (BCHARGE) required for system shutdown",
        )
        self.gauge_mintimel = Gauge(
            name="apcups_mintimel",
            documentation="Min battery runtime (MINUTES) required for system shutdown",
        )
        self.gauge_maxtime = Gauge(
            name="apcups_maxtime",
            documentation="Max battery runtime (TIMEOUT) after which system is shutdown",
        )
        self.gauge_battv = Gauge(
            name="apcups_battv", documentation="Current battery voltage"
        )

    def status(self, vals: str):
        sum = 0
        for val in vals.split(","):
            if val == "ONLINE":
                sum += 1
        return sum

    def translate(self, key: str, val: str):
        """https://manpages.ubuntu.com/manpages/bionic/man8/apcaccess.8.html"""
        if key == "APC":
            self.APC = val
        if key == "DATE":
            self.DATE = val
        if key == "HOSTNAME":
            self.HOSTNAME = val
        if key == "VERSION":
            self.VERSION= val
        if key == "HOSTNAME":
            self.HOSTNAME = val
        if key == "STATUS":
            self.gauge_status.set(self.status(val))
        if key == "LINEV":
            self.gauge_linev.set(val.split(" ")[0])
        if key == "LOADPCT":
            self.gauge_loadpct.set(val.split(" ")[0])
        if key == "BCHARGE":
            self.gauge_bcharge.set(val.split(" ")[0])
        if key == "TIMELEFT":
            self.gauge_timeleft.set(val.split(" ")[0])
        if key == "MBATTCHG":
            self.gauge_mbattchg.set(val.split(" ")[0])
        if key == "MINTIMEL":
            self.gauge_mintimel.set(val.split(" ")[0])
        if key == "MAXTIME":
            self.gauge_maxtime.set(val.split(" ")[0])
        if key == "BATTV":
            self.gauge_battv.set(val.split(" ")[0])

    def apcaccess(self):
        proc = subprocess.Popen(
            ["apcaccess"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
        )
        output = proc.stdout.readlines()
        for line in output:
            key, val = line.split(":", 1)
            key = key.strip()
            val = val.strip()
            self.translate(key, val)
        return self.APC, self.DATE, self.HOSTNAME, self.VERSION, self.UPSNAME

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    EXPORTER_PORT = int(os.getenv("EXPORTER_PORT", "8000"))
    POLLING_INTERVAL = int(os.getenv("POLLING_INTERVAL", "60"))

    apc = APCUPS()

    start_http_server(port=EXPORTER_PORT, addr="0.0.0.0")
    while True:
        vals = apc.apcaccess()
        logging.info("%s:%s", datetime.now(), len(vals))
        time.sleep(POLLING_INTERVAL)
