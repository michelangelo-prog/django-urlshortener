# django-urlshortener

## Commands description - start local

### Run and build containers
```sh
docker-compose up --build
```

### Apply migrations
```sh
docker exec -it urlshortener-app python manage.py migrate
```

### Create admin user
```sh
docker exec -it urlshortener-app python manage.py createsuperuser
```

Access the application at the address [http://localhost:8000/](http://localhost:8000/)

Access the admin site at the adress [http://localhost:8000/admin/login/?next=/admin/](http://localhost:8000//admin/login/?next=/admin/)