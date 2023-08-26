# Проект QRKot
Фонд собирает пожертвования на различные целевые проекты: на медицинское обслуживание нуждающихся хвостатых, на обустройство кошачьей колонии в подвале, на корм оставшимся без попечения кошкам — на любые цели, связанные с поддержкой кошачьей популяции.

Для просмотра документации перейдите на главную страницу проекта

## Технологии
- Python
- FastAPI
- Alembic
- SQLAlchemy
- Uvicorn


## Запуск проекта

- Клонировать репозиторий и перейти в него в командной строке:

```python
git clone git@github.com:Bacepok/cat_charity_fund.git
cd cat_charity_fund
```

- Cоздать и активировать виртуальное окружение:

```python
python -m venv venv
source venv/Scripts/activate
```

- Установить зависимости из файла requirements.txt:

```python
python -m pip install --upgrade pip
pip install -r requirements.txt
```

- создать файл .env и заполнить его по шаблону:

```python
touch .env
```

шаблон заполнения env-файла:

```python
APP_TITLE=Кошачий благотворительный фонд
DATABASE_URL=описание подключения к базе данных, по умолчанию в проекте стоит база данных sqlite+aiosqlite:///./base.db, вы можете установить свою
SEKRET=секретный ключ
```

- Выполнить миграции:

```python
alembic init
alembic upgrade head
```

- Запустить проект:

```python
uvicorn app.main:app --reload
```

Проект будет доступен локально по адресу:
http://127.0.0.1:8000/