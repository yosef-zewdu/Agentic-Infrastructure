.PHONY: setup docker-build test spec-check

IMAGE_NAME = dy1-test:latest

setup:
	pip install -r requirements.txt

docker-build:
	docker build -t $(IMAGE_NAME) .

test: docker-build
	# Run tests inside a container to ensure environment parity
	docker run --rm -v $(PWD):/app -w /app $(IMAGE_NAME) pytest -q

spec-check: docker-build
	# Run the spec-check script inside the container
	docker run --rm -v $(PWD):/app -w /app $(IMAGE_NAME) python scripts/spec_check.py
