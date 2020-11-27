FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /

RUN apt-get update && apt-get upgrade -y
RUN curl -SLO https://github.com/jgm/pandoc/releases/download/2.11.1.1/pandoc-2.11.1.1-1-amd64.deb && \
    dpkg -i pandoc-2.11.1.1-1-amd64.deb && \
    rm -Rf pandoc-2.11.1.1-1-amd64.deb
# RUN apt-get install -y nginx
# COPY nginx/nginx.conf /etc/nginx/nginx.conf
# COPY nginx/conf.d /etc/nginx/conf.d

RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

COPY ./docker-entrypoint.sh .
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]