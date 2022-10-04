## ⚙️ Setup
В дериктории с проектом необходимо создать `.env` файл с содержимым:
- SECRET_KEY=XXXXXXXXXXXXXXXXXXXX
- DEBUG=XXXX (bool)
- REDIS_URL=XXXXXXX
- REDIS_PORT=XXXXXXX



Пропишите эти команды по очередности:

    python manage.py makemigrations
    
    python manage.py migrate
    
    python manage.py runserver

    celery -A core worker --beat -l INFO