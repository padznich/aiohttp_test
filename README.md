# Polls

Setup
---
- $ python3 --version
    - Python 3.5.2
- virtualenv -p python3 venv
- (venv) pip install -r requirements.txt
- sudo -u postgres psql postgres < sql/init_db.sql
- sudo -u postgres psql postgres -d polls < sql/create_tables.sql
- config/polls.yaml
- 

Run
---

    $ gunicorn wsgi:app --bind 0.0.0.0:8080 --worker-class aiohttp.worker.GunicornWebWorker

Testing
___
    $ pytest tests/unit/*.py
    $ pytest tests/integration/*.py
    $ tox -e pep8