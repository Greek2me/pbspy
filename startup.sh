#!/bin/bash

TESTFILE=/opt/civ4/data/INITIALIZED

cd /opt/civ4/

# Initialize database if required.
if [ ! -f $TESTFILE ]; then
	echo "Initializing database."
	mkdir /opt/civ4/data
        python3 manage.py migrate
        python3 manage.py migrate static_precompiler
        python3 manage.py compilestatic
        #python3 manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@localhost', '${ADMIN_PASSWORD}')"
	touch $TESTFILE
fi

# Run server.
python3 /opt/civ4/manage.py runserver 0.0.0.0:${DJANGO_PORT}
