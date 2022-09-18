.PHONY: install
install:
	git clone https://github.com/mamercad/apcups-prometheus-exporter.git
	cd apcups-prometheus-exporter
	cp docker/prometheus_apcups_exporter.py /usr/local/bin/prometheus_apcups_exporter.py
	cp systemd/apcups-prometheus-exporter.service /etc/systemd/system/apcups-prometheus-exporter.service
	systemctl daemon-reload
	systemctl enable apcups-prometheus-exporter
	systemctl start apcups-prometheus-exporter
