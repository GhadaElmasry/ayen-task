#!/bin/bash

function postgres_setup(){
python << END
import sys
import psycopg2
import environ
try:
    ROOT_DIR = environ.Path(__file__) - 3
    APPS_DIR = ROOT_DIR.path('src')
    ENV_PATH = str(APPS_DIR.path('.env'))
    env = environ.Env()
    if env.bool('READ_ENVFILE', default=True):
        env.read_env(ENV_PATH)
    conn = psycopg2.connect(dbname=env('POSTGRES_DATABASE', default=''), user=env('POSTGRES_USER', default=''), password=env('POSTGRES_PASSWORD', default=''), host="ayen_db")
except psycopg2.OperationalError:
    sys.exit(-1)
sys.exit(0)
END
}

# migrate any changes to the database container
python /src/manage.py migrate --noinput
rc=$?; if [[ $rc != 0 ]]; then exit $rc; fi

# load data if LOAD_DATA is on
if [ "x$LOAD_DATA" = 'xon' ]; then
    python /src/manage.py loaddata /src/fixtures/*.json
fi

# collect static files
find . -name '*.pyc' -delete && \
    python /src/manage.py --findstatic

uwsgi --http-auto-chunked --http-keepalive --buffer-size=7000 --static-map /static=/src/static --static-map /media=/src/media