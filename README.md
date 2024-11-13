Requerimentos:
django -> pip install django
postgres -> pip install psycopg2

// Caso for usar outro tipo de banco, o psycopg2 não vai servir. Falar comigo.

COMANDOS VIA TERMINAL:

para fazer as migrações do banco
- python manage.py makemigrations
- python manage.py migrate

para criar um superUser:
- python manage.py createsuperuser
- preencher as informações

para rodar o servidor local:
- python manage.py runserver

user e password serão acessadas pelo superUser criado.
