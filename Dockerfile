FROM python:3.9

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
COPY . /code/

# install python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt




# running migrations
# RUN python manage.py makemigrations
# RUN python manage.py migrate

# gunicorn
CMD ["gunicorn","-c", "config/gunicorn/conf.py","--bind",":8000","--chdir","django_portal_wallpapers","admin_wallpaper.wsgi:application"]

