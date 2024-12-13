Commands to run the project:

1. python -m venv venv
2. venv\Scripts\activate (windows) or source venv/bin/activate (mac/linux)
3. pip install -r requirements.txt
4. python manage.py makemigrations
5. python manage.py migrate
6. python manage.py import_data data/data.csv
7. python manage.py runserver

Command to run the tests:

1. python manage.py test
