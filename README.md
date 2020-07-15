# django-urlshortener

## Commands description 

### Run and build containers - start local
```sh
docker-compose -f docker-compose.yml up --build
```

### Run and build containers - start prod, before run edit envs
```sh
docker-compose -f docker-compose.prod.yml up --build
```

### Apply migrations
```sh
docker exec -it urlshortener-app python manage.py migrate
```

### Create admin user
```sh
docker exec -it urlshortener-app python manage.py createsuperuser
```

### Local

Access the application at the address [http://localhost:8000/](http://localhost:8000/)

Access the admin site at the adress [http://localhost:8000/admin/](http://localhost:8000/admin/)


### Prod
```sh
docker exec -it urlshortener-app python manage.py collectstatic
```