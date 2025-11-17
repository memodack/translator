include .env

export $(shell sed 's/=.*//' .env)

dev:
	docker compose up --remove-orphans dev

build:
	docker buildx build --platform linux/amd64,linux/arm64 -t ghcr.io/memodack/translator:$(VERSION) --push . --provenance=false