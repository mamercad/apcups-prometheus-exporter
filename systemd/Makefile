.PHONY: install
install:
	sudo mkdir /opt/apcups-prometheus-exporter
	sudo python3 -m venv /opt/apcups-prometheus-exporter/venv
	git clone https://github.com/mamercad/apcups-prometheus-exporter.git
	cd apcups-prometheus-exporter
	sudo /opt/apcups-prometheus-exporter/venv/bin/pip3 install --requirement docker/requirements.txt
	sudo cp docker/prometheus_apcups_exporter.py /usr/local/bin/prometheus_apcups_exporter.py
	sudo cp systemd/apcups-prometheus-exporter.service /etc/systemd/system/apcups-prometheus-exporter.service
	sudo systemctl daemon-reload
	sudo systemctl enable apcups-prometheus-exporter
	sudo systemctl start apcups-prometheus-exporter
