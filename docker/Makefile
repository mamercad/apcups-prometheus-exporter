IMAGE = ghcr.io/mamercad/apcups-prometheus-exporter:devel

.PHONY: requirements
requirements:
	poetry export \
		--format requirements.txt \
		--output requirements.txt \
		--without-hashes

.PHONY: build
build:
	docker build \
		--tag $(IMAGE) .

.PHONY: run
run:
	docker run \
		--rm --interactive --tty \
		--publish 8000:8000/tcp \
		$(IMAGE)
