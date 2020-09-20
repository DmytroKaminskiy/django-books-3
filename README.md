# django-books-3

1. Добавить поле phone в модель User (CharField(max_length=30))
2. Создать сигнал User/pre_save который будет "чистить" поле phone (оставить только цифры)
3. Создать модель Logger с полями
   method = {"GET", "POST"} - request.method
   path = "/users/list/" - request.path
   response_time = время работы вью функции
   created = время создания записи в БД.
4. Сохранять каждый запрос в таблицу Logger (использовать Middlewares)