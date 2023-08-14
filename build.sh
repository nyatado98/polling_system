 python3.9 -m venv virtual
 
 python3.9 -m pip install -r requirements-production.txt
 python3.9 manage.py collectstatic --noinput --clear