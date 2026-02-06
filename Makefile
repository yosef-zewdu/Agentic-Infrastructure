.PHONY: setup docker-build test spec-check

IMAGE_NAME = agentic-infrastructure-test:latest

setup:
	pip install -r requirements.txt

docker-build:
	docker build -t $(IMAGE_NAME) .

test: docker-build
	@echo "Run tests inside a container to ensure environment parity"
	docker run --rm  $(IMAGE_NAME) 
