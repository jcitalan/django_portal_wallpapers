# Django Portal Wallpaper
- `Deployment`: **Docker**, Gunicorn / Nginx
<br />

## ✨ Quick Start in `Docker`

> Get the code
>open a new command prompt
```bash
$ docker-compose up --build 
```


## ✨ Create Django Migrations
>open a other new command prompt
```bash
$ # Get the code
$ docker exec -it container_id(app) python manage.py makemigrations
$ docker exec -it container_id(app) python manage.py migrate
$ docker exec -it  container_id(app) python manage.py createsuperuser
$ docker exec -it container_id(app) python manage.py collectstatic --noinput
$ # Access the web app in browser: http://127.0.0.1:8000/
```
Visit `http://127.0.0.1:8000 in your browser. The app should be up & running.
