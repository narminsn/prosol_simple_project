# prosol_simple_project

1. Clone project.
2. Create virtual env.
~~~python
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
~~~
3. Create environment variables (.env)
4. Migrate db
~~~python
python3 manage.py migrate
~~~
5. Run project
~~~python
python3 manage.py runserver
~~~
