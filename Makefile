.PHONY: up, down, up-dev, down-dev, run, fmt

run:
	uvicorn src.main:app --port 8080 --reload

up:
	docker compose -f ./compose-local.yml -p local up -d

down:
	docker compose -f ./compose-local.yml -p local down

up-dev:
	docker compose -f ./compose-dev.yml -p dev up -d

down-dev:
	docker compose -f ./compose-local.yml -p dev down

fmt:
	ruff format; ruff check --fix
