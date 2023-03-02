format:
	black .
	isort .

pytest:
	pytest -vv

coverage:
	pytest --cov=profiles -vv

install:
	@pip install -r requirements.txt

migrate:
	python manage.py migrate

runserver:
	python manage.py runserver

build:
	@pip install -r requirements.txt
	python manage.py migrate
