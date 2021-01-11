FROM python:3.9.0-slim
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install curl -y && \
    curl -SLO https://github.com/jgm/pandoc/releases/download/2.11.1.1/pandoc-2.11.1.1-1-amd64.deb && \
    dpkg -i pandoc-2.11.1.1-1-amd64.deb && \
    rm -Rf pandoc-2.11.1.1-1-amd64.deb && \
    apt-get autoremove --purge && \
    apt-get -y clean

COPY . ./code
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r ./code/requirements.txt

CMD ["tail", "-f"]

# EXPOSE 8000
# RUN chmod +x ./docker-entrypoint.sh
# ENTRYPOINT ["/code/docker-entrypoint.sh"]
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]







# ENV VIRTUAL_ENV=/opt/venv
# WORKDIR /code

# RUN python3 -m venv $VIRTUAL_ENV
# ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# RUN apt-get install -y nginx
# COPY nginx/nginx.conf /etc/nginx/nginx.conf
# COPY nginx/conf.d /etc/nginx/conf.d

# COPY . /code
# COPY requirements.txt ./

# RUN touch test.txt
# RUN echo | pwd
# CMD ["tail", "-f", "requirements.txt"]

# COPY . ./code
# COPY requirements.txt ./
# RUN pip install --upgrade pip && \
#     pip install --no-cache-dir -r ./code/requirements.txt

# RUN pip install -r /code/requirements.txt

# CMD ["tail", "-f"]

# EXPOSE 8000
# RUN chmod +x docker-entrypoint.sh
# ENTRYPOINT ["/code/docker-entrypoint.sh"]

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


# COPY requirements.txt .
# RUN pip install -r requirements.txt
# COPY . /code

# COPY ./docker-entrypoint.sh /
# RUN chmod +x /docker-entrypoint.sh
# ENTRYPOINT ["/docker-entrypoint.sh"]


# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]