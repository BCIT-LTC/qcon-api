FROM python:3.9 AS qcon-base

ENV ARCH amd64
ENV PANDOC_VERSION 2.11.3.2
ENV GET_PANDOC_URL https://github.com/jgm/pandoc/releases/download

RUN set -ex \
    && apt-get update \
    && apt-get install -y --no-install-recommends build-essential gcc wget \
    && wget -O pandoc.deb "$GET_PANDOC_URL/$PANDOC_VERSION/pandoc-$PANDOC_VERSION-1-$ARCH.deb" \
    && dpkg -i pandoc.deb \
    && rm -Rf pandoc.deb \
    && apt-get autoremove --purge \
    && apt-get -y clean

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt


#######################################################
FROM squidfunk/mkdocs-material as docs-base

RUN pip install Pygments pymdown-extensions

WORKDIR /docs

COPY . .

RUN mkdocs build --site-dir /public


#######################################################
FROM python:3.9-alpine AS release  
LABEL maintainer courseproduction@bcit.ca

ENV PYTHONUNBUFFERED 1
ENV PATH /code:$PATH
RUN apk --update add nginx bash

WORKDIR /code
VOLUME /code

COPY --from=qcon-base /usr/bin/pandoc /usr/local/bin/pandoc
COPY --from=qcon-base /root/.cache /root/.cache
COPY --from=qcon-base /opt/venv /opt/venv
ENV PATH /opt/venv/bin:$PATH
COPY --from=docs-base public docs/public

COPY /nginx/nginx.conf /etc/nginx/nginx.conf

COPY manage.py .
COPY qcon qcon
COPY api_v2 api_v2
COPY .env .env

COPY docker-entrypoint.sh /usr/local/bin
ENTRYPOINT ["docker-entrypoint.sh"]

EXPOSE 8000
CMD ["nginx", "-g", "daemon off;"]
