backend-dev:
	docker exec -it wish-framework-portal sudo --preserve-env=PYTHONPATH /home/app/virtualenv/bin/uwsgi --http 0.0.0.0:8000 --wsgi-file /home/app/wish-framework-portal/app/backend/wsgi.py --callable app --threads 8

frontend-install:
	docker exec -w /home/app/wish-framework-portal/app/frontend -it wish-framework-portal npm install

frontend-dev:
	docker exec -w /home/app/wish-framework-portal/app/frontend -it wish-framework-portal npm run serve

nginx:
	sudo service nginx start

dnsproxy:
	sudo python2 /home/app/marlon-tools/tools/dnsproxy/dnsproxy.py -s 127.0.0.11 -H 0.0.0.0 --hosts-file=/home/app/wish-framework-portal/app/backend/config/hosts &

backend:
	sudo --preserve-env=PYTHONPATH /home/app/virtualenv/bin/uwsgi --http 0.0.0.0:8000 --wsgi-file /home/app/wish-framework-portal/app/backend/wsgi.py --callable app --threads 8 &

frontend:
	cd /home/app/wish-framework-portal/app/frontend && npm run serve &

all: nginx dnsproxy backend  frontend
