**This project is developed on python 3.6

How to run the project

** Use virtual environment for isolated local development

pip install -r requirements.txt
python manage.py makemigrations customer (Before running this command set database connection properly in settings.py file)
python manage.py migrate
python manage.py runserver_plus localhost:8000 (For development)

or 

python manage.py runserver