
Docker-образ приложения, которое будет при запуске контейнера скачивать favicon заданного приложению сайта.


Сборка docker-образа
```
docker build --tag python-favicon .
```

Запуск контейнера
```
docker run -v <local_path>:/app/images --rm python-favicon <domain>
```
