FROM python:3.9 AS qcon-base

ENV ARCH amd64
ENV PANDOC_VERSION 2.11.3.2
ENV GET_PANDOC_URL https://github.com/jgm/pandoc/releases/download

RUN set -ex \
    && apt-get update \
    # && apt-get install -y nginx \
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
FROM python:3.9-alpine AS release  
LABEL maintainer courseproduction@bcit.ca

ENV PYTHONUNBUFFERED 1
ENV PATH /code:$PATH

WORKDIR /code
VOLUME /code

COPY --from=qcon-base /usr/bin/pandoc /usr/local/bin/pandoc
COPY --from=qcon-base /root/.cache /root/.cache
COPY --from=qcon-base /opt/venv /opt/venv
ENV PATH /opt/venv/bin:$PATH

 
RUN mkdir -p log && touch log/error.log \
    && chmod g+w log/error.log

COPY /nginx/nginx.conf /etc/nginx/nginx.conf
COPY . .

COPY docker-entrypoint.sh /usr/local/bin
ENTRYPOINT ["docker-entrypoint.sh"]

EXPOSE 8000
# CMD ["python","manage.py","runserver","0.0.0.0:8000"]
CMD ["nginx", "-g", "daemon off;"]