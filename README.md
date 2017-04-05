# Polls

Setup
---
- $ python3 --version
    - Python 3.5.2
- virtualenv -p python3 venv
- (venv) pip install -r requirements.txt
- sudo -u postgres psql postgres < polls/sql/init_db.sql
- sudo -u postgres psql postgres -d polls < polls/sql/create_tables.sql

Run
---

    $ gunicorn wsgi:app --bind 0.0.0.0:8080 --worker-class aiohttp.worker.GunicornWebWorker

Testing
___
    $ pytest -v
    $ pytest -v --pep8