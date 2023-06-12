import csv
import logging

from django.core.management.base import BaseCommand, CommandError

from reviews.models import Category, Comment, Genre, Review, Title
from user.models import User

logging.basicConfig(
    level=logging.INFO,
    filename='main.log',
    format='%(asctime)s, %(levelname)s, %(name)s, %(message)s',
    filemode='w',
    encoding='utf-8',
)

CSV_PATH = 'static/data/'

FOREIGN_KEY_FIELDS = ('category', 'author')

DICT = {
    User: 'users.csv',
    Genre: 'genre.csv',
    Category: 'category.csv',
    Title: 'titles.csv',
    Review: 'review.csv',
    Comment: 'comments.csv',
}


def csv_serializer(csv_data, model):
    objs = []
    for row in csv_data:
        for field in FOREIGN_KEY_FIELDS:
            if field in row:
                row[f'{field}_id'] = row[field]
                del row[field]
        objs.append(model(**row))
    model.objects.bulk_create(objs)


class Command(BaseCommand):
    help = 'Загрузка информации из csv файлов в БД'

    def handle(self, *args, **kwargs):
        for model in DICT:
            try:
                with open(
                    CSV_PATH + DICT[model],
                    newline='',
                    encoding='utf8',
                ) as csv_file:
                    csv_serializer(csv.DictReader(csv_file), model)
            except Exception as error:
                CommandError(error)
        logging.info('Все данные успешно загружены в БД')
