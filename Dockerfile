FROM python:3.9 AS qcon-base

ENV ARCH amd64
ENV PANDOC_VERSION 2.11.3.2
ENV GET_PANDOC_URL https://github.com/jgm/pandoc/releases/download
ENV PATH="/opt/venv/bin:/base:$PATH"

WORKDIR /base

COPY requirements.txt .

RUN set -ex \
    && apt-get update \
    && apt-get install -y --no-install-recommends build-essential gcc wget jq git \
    && wget -O pandoc.deb "$GET_PANDOC_URL/$PANDOC_VERSION/pandoc-$PANDOC_VERSION-1-$ARCH.deb" \
    && dpkg -i pandoc.deb \
    && rm -Rf pandoc.deb \
    && apt-get autoremove --purge \
    && apt-get -y clean \
    && python -m venv /opt/venv \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

COPY .git/ ./.git/
COPY .build_status.json .

RUN echo `pwd`
RUN echo `ls -lah`
RUN set -ex \
    PROJECT_NAME=$(basename $(pwd)) \
    GIT_VERSION=$(git tag --sort=committerdate | tail -1) \
    GIT_HASH=$(git rev-parse HEAD) \
    GIT_SHORT_SHA=$(git rev-parse --short HEAD) \
    GIT_BUILD_TIME=$(git show -s --format=%cs $GIT_HASH) \
    BUILD_STATUS=$(jq \
    --arg name "$PROJECT_NAME" \
    --arg version "$GIT_VERSION" \
    --arg hash "$GIT_HASH" \
    --arg short_sha "$GIT_SHORT_SHA" \
    --arg build_time "$GIT_BUILD_TIME" \
    '.name |= $name | .version.number |= $version | .version.build_hash |= $hash | .version.build_short_sha |= $short_sha | .version.build_timestamp |= $build_time' .build_status.json) \
    && echo $BUILD_STATUS > .build_status.json


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
ENV PATH /code:/opt/venv/bin:$PATH

WORKDIR /code
# VOLUME /code

RUN apk --update add nginx bash \
    && chmod -R 755 /var/lib/nginx

COPY /nginx/nginx.conf /etc/nginx/nginx.conf
COPY manage.py .
COPY supervisord.conf .
COPY .env .env
COPY docker-entrypoint.sh /usr/local/bin
COPY --from=qcon-base /usr/bin/pandoc /usr/local/bin/pandoc
COPY --from=qcon-base /root/.cache /root/.cache
COPY --from=qcon-base /opt/venv /opt/venv
COPY --from=docs-base public docs/public
COPY --from=qcon-base .build_status.json .build_status.json
COPY qcon qcon
COPY api_v2 api_v2

ENTRYPOINT ["docker-entrypoint.sh"]

EXPOSE 8000
CMD ["supervisord", "-c", "supervisord.conf", "-n"]