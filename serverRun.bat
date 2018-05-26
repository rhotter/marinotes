
start chrome -incognito http://127.0.0.1:5000/share
set FLASK_APP=application.py
set FLASK_DEBUG=1
python -m flask run
