
FROM python:3
ENV PYTHONUNBUFFERED 1
# RUN mkdir /code
WORKDIR /

RUN apt-get update && apt-get upgrade -y

# RUN apt-get install -y nginx
# COPY nginx/nginx.conf /etc/nginx/nginx.conf
# COPY nginx/conf.d /etc/nginx/conf.d

RUN pip install --upgrade pip

COPY requirements.txt /
RUN pip install -r requirements.txt
COPY . /

# RUN apt-get install -y postgresql-client-11

# RUN curl -sL https://deb.nodesource.com/setup_lts.x | bash -
# RUN apt-get install -y nodejs

# EXPOSE 8080

COPY ./docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/bin/sh", "/docker-entrypoint.sh"]