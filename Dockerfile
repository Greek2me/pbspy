FROM ubuntu:jammy

# Copy requirements list.
COPY requirements.txt /opt/civ4/requirements.txt

# Install dependencies.
RUN apt-get update && apt-get install -y python3-pip pkg-config node-less default-libmysqlclient-dev && pip install -r /opt/civ4/requirements.txt

# Copy files.
COPY civdj /opt/civ4/civdj
COPY pbspy /opt/civ4/pbspy
COPY manage.py /opt/civ4/manage.py
COPY PBSpyIcon.xcf /opt/civ4/PBSpyIcon.xcf
COPY startup.sh /opt/civ4/startup.sh
RUN chmod +x /opt/civ4/startup.sh

# Take arguments.
ARG PORT=8080

# Copy arguments to environment.
ENV DJANGO_PORT ${PORT}

# Expose Port
EXPOSE $PORT

# Run startup script.
CMD ["/bin/sh", "-c", "exec /opt/civ4/startup.sh"]
