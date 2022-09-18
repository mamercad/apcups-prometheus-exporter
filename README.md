# [Prometheus](https://prometheus.io) Exporter for APC UPSs

[![docker-image](https://github.com/mamercad/apcups-prometheus-exporter/actions/workflows/docker-image.yml/badge.svg)](https://github.com/mamercad/apcups-prometheus-exporter/actions/workflows/docker-image.yml)

[Prometheus](https://prometheus.io) metrics of your APC UPS data.

There's Docker stuff [here](./docker), Kubernetes stuff [here](./kubernetes), and SystemD stuff [here](./systemd).

It behaves like this:

```bash
❯ curl -s 192.168.1.181:8000 | grep ^apcups
apcups_status 1.0
apcups_linev 115.0
apcups_loadpct 9.0
apcups_bcharge 100.0
apcups_timeleft 75.0
apcups_mbattchg 5.0
apcups_mintimel 3.0
apcups_maxtime 0.0
apcups_battv 27.3
```
