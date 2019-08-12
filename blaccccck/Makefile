.PHONY: black diff run

black:
	docker-compose up -d develop
	docker-compose exec develop poetry install
	docker-compose exec develop poetry run black .

diff:
	docker-compose up -d develop
	docker-compose exec develop poetry install
	docker-compose exec develop poetry run black --diff .

run:
	docker-compose up -d develop
	docker-compose exec develop poetry install
	docker-compose exec develop poetry run python foo.py
