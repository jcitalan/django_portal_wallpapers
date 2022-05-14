# Django Portal Wallpaper
- `Deployment`: **Docker**, Gunicorn / Nginx
<br />

## ✨ Quick Start in `Docker`

> Get the code
>open a new command prompt
```bash
$ docker-compose up --build 
```


## ✨ Create SuperUser Django
>open a other new command prompt
```bash
$ # Get the code
$ docker exec -it  container_id(app) python manage.py createsuperuser
```
Visit http://127.0.0.1:8000 in your browser. The app should be up & running.
