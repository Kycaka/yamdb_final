[![Django-app workflow](https://github.com/Kycaka/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)](https://github.com/Kycaka/yamdb_final/actions/workflows/yamdb_workflow.yml)

# API_YAMDB
REST API проект для сервиса YaMDb — сбор отзывов о фильмах, книгах или музыке.

## Описание

Проект YaMDb собирает отзывы пользователей на произведения.
Произведения делятся на категории: «Книги», «Фильмы», «Музыка».
Список категорий  может быть расширен (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»).
### Как запустить проект:

Все описанное ниже относится к ОС Linux.
Клонируем репозиторий и переходим в него:
```bash
git clone https://github.com/Kycaka/infra_sp2
cd infra_sp2
cd api_yamdb
```

Перейти в папку:
```
cd infra
```
Развернуть контейнеры:
```
docker-compose up 
```
Сделать миграции, суперпользователя и собрать статику:
```
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input
```

### Шаблон наполнения .env (не включен в текущий репозиторий) расположенный по пути infra/.env
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```

### Документация API YaMDb
Документация доступна по эндпойнту: http://localhost/redoc/

### Server IP 84.201.131.143
