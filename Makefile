mig:
	python3 manage.py makemigrations
	python3 manage.py migrate
admin:
	python3 manage.py createsuperuser
celery:
	celery -A root worker -l INFO --concurrency=4 -Q high_priority -n worker1
	celery -A root worker -l INFO --concurrency=1 -Q low_priority -n worker3
