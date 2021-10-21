FROM python:3.9 AS qcon-api-base

ENV ARCH amd64
ENV PANDOC_VERSION 2.11.3.2
ENV GET_PANDOC_URL https://github.com/jgm/pandoc/releases/download
ENV PATH="/opt/venv/bin:/base:$PATH"

# Set to project name
WORKDIR /qcon-api

COPY requirements.txt .build_status.json ./

RUN set -ex; \
        apt-get update; \
        apt-get install -y --no-install-recommends \
            build-essential \
            gcc \
            wget \
            jq \
            git \
        ; \
        wget -O pandoc.deb \
            "$GET_PANDOC_URL/$PANDOC_VERSION/pandoc-$PANDOC_VERSION-1-$ARCH.deb"; \
        dpkg -i pandoc.deb; \
        rm -Rf pandoc.deb; \
        \
        apt-get autoremove --purge; \
        apt-get -y clean; \
        \
        python -m venv /opt/venv; \
        \
        pip install --upgrade pip; \
        pip install -r requirements.txt; 


#######################################################
FROM python:3.9-alpine AS release  
LABEL maintainer courseproduction@bcit.ca

ENV PYTHONUNBUFFERED 1
ENV PATH /code:/opt/venv/bin:$PATH

WORKDIR /code

RUN apk --update add \
        nginx \
        bash; \
    chmod -R 755 /var/lib/nginx;

COPY /nginx/nginx.conf /etc/nginx/nginx.conf
COPY --from=qcon-api-base /usr/bin/pandoc /usr/local/bin
COPY --from=qcon-api-base /root/.cache /root/.cache
COPY --from=qcon-api-base /opt/venv /opt/venv
COPY docker-entrypoint.sh /usr/local/bin
COPY manage.py supervisord.conf ./
COPY qcon qcon
COPY api_v2 api_v2
COPY .build_status.json ./
COPY .env ./

ENTRYPOINT ["docker-entrypoint.sh"]

EXPOSE 8000
CMD ["supervisord", "-c", "supervisord.conf", "-n"]