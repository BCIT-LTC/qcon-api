FROM python:3.9 AS qcon-api-base

ENV ARCH amd64
ENV PANDOC_VERSION 2.11.3.2
ENV GET_PANDOC_URL https://github.com/jgm/pandoc/releases/download
ENV PATH="/opt/venv/bin:/base:$PATH"

# Set to project name
WORKDIR /qcon-api

COPY requirements.txt .build_status.json .git .

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
        pip install -r requirements.txt; \
        \
        git fetch origin main --tags; \
        \
        PROJECT_NAME="$(basename $(pwd))"; \
        echo $(git describe --tags $(git rev-list --tags --max-count=1)) > newtags.txt; \
        GIT_VERSION="$(echo $(cat newtags.txt))"; \
        GIT_HASH="$(git rev-parse HEAD)"; \
        GIT_SHORT_SHA="$(git rev-parse --short HEAD)"; \
        GIT_BUILD_TIME="$(git show -s --format=%cs $GIT_HASH)"; \
        BUILD_STATUS="$(jq \
            --arg name "$PROJECT_NAME" \
            --arg version "$GIT_VERSION" \
            --arg hash "$GIT_HASH" \
            --arg short_sha "$GIT_SHORT_SHA" \
            --arg build_time "$GIT_BUILD_TIME" \
            '.name |= $name \
            | .version.number |= $version \
            | .version.build_hash |= $hash \
            | .version.build_short_sha |= $short_sha \
            | .version.build_timestamp |= $build_time' .build_status.json)"; \
        echo $BUILD_STATUS > .build_status.json;


#######################################################
FROM squidfunk/mkdocs-material as docs-base

RUN pip install \
        Pygments \
        pymdown-extensions;

WORKDIR /docs

COPY . .

RUN mkdocs build \
        --site-dir /public;


#######################################################
FROM python:3.9-alpine AS release  
LABEL maintainer courseproduction@bcit.ca

ENV PYTHONUNBUFFERED 1
ENV PATH /code:/opt/venv/bin:$PATH

WORKDIR /code
# VOLUME /code

RUN apk --update add \
        nginx \
        bash; \
    chmod -R 755 /var/lib/nginx;

COPY --from=docs-base public docs/public
COPY /nginx/nginx.conf /etc/nginx/nginx.conf
COPY --from=qcon-api-base /usr/bin/pandoc /usr/local/bin
COPY --from=qcon-api-base /root/.cache /root/.cache
COPY --from=qcon-api-base /opt/venv /opt/venv
COPY docker-entrypoint.sh /usr/local/bin
COPY manage.py supervisord.conf .env qcon api_v2 .
COPY --from=qcon-api-base /qcon-api/.build_status.json .

ENTRYPOINT ["docker-entrypoint.sh"]

EXPOSE 8000
CMD ["supervisord", "-c", "supervisord.conf", "-n"]