# YaMDb API
##### В этом проекте реализован API для небольшой социальной сети YaMDb. В YaMDb пользователи могут писать рецензии к различным произведениям (книги, музыка, фильмы и т.д.), а также оставлять к рецензиям комментарии. Сами произведения в YaMDb не хранятся.  

### Технологии:
``Python 3.7``; ``Django``; ``Django REST Framework``; ``SQLite``; ``Simple-JWT``

### Больше информации:
Подробная документация к API после запуска проекта доступна по адресу http://127.0.0.1:8000/redoc/

### Запуск проекта:
Клонировать репозиторий и перейти командой:

```
git clone https://github.com/4uku/api_yamdb.git
```

```
cd api_yamdb
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```
