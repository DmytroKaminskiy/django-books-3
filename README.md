# django-books-3

1. flake8 (flake8, flake8-builtins, flake8-import-order, flake8-print)
2. Travis CI
3. Создать команду generate_books (10_000)

БОНУС
  3.1 Передавать пармаетр в команду который регулирует количество создавемых книг
  python src/manage.py generate_books 100 (по-умолчанию 1_000)
  python src/manage.py generate_books (по-умолчанию 1_000)
  3.2 Использовать в команде Book.objects.bulk_create()
  https://docs.djangoproject.com/en/3.0/ref/models/querysets/#bulk-create
