# prosol_simple_project

1. Clone project.
~~~python
2. cd prosol_simple_project/
~~~

3. Create virtual env.
~~~python
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
~~~
4. Create environment variables (.env)
~~~python
POSTGRES_DB
POSTGRES_USER
POSTGRES_PASSWORD
POSTGRES_HOST
POSTGRES_PORT
~~~

5. Migrate db
~~~python
python3 manage.py migrate
~~~
6. Create admin user
~~~python
python3 manage.py createsuperuser
~~~
7. Run project
~~~python
python3 manage.py runserver
~~~
