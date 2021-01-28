FROM python:3.9-slim AS qcon-base

ENV ARCH amd64
ENV PANDOC_VERSION 2.11.3.2
ENV GET_PANDOC_URL https://github.com/jgm/pandoc/releases/download

RUN set -ex \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
        wget \
    && wget -O pandoc.deb "$GET_PANDOC_URL/$PANDOC_VERSION/pandoc-$PANDOC_VERSION-1-$ARCH.deb" \
    && dpkg -i pandoc.deb \
    && rm -Rf pandoc.deb \
    && apt-get autoremove --purge \
    && apt-get -y clean

WORKDIR /code

# Copy in new files
COPY requirements.txt .

RUN mkdir log \
    && touch log/error.log \
    && chmod g+w log/error.log

RUN pip install -r requirements.txt

#
#
#
#
FROM python:3.9-alpine AS release  

LABEL maintainer courseproduction@bcit.ca

ENV PYTHONUNBUFFERED 1

WORKDIR /code

EXPOSE 8000

COPY --from=qcon-base /usr/bin/pandoc /usr/local/bin/pandoc
COPY --from=qcon-base /root/.cache /root/.cache

# Re-run requirements install with cached wheels
COPY requirements.txt .
RUN pip install -r requirements.txt

# Finally copy in our code
COPY . .
RUN chmod +x /code/docker-entrypoint.sh

ENTRYPOINT ["/code/docker-entrypoint.sh"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]