FROM python:3.10 AS qcon-api-base

ENV ARCH amd64
ENV PANDOC_VERSION 2.16.1
ENV GET_PANDOC_URL https://github.com/jgm/pandoc/releases/download
ENV PATH="/opt/venv/bin:/base:$PATH"

# Set to project name
WORKDIR /qcon-api

COPY requirements.txt ./

RUN set -ex; \
        apt-get update; \
        apt-get install -y --no-install-recommends \
            build-essential \
            gcc \
            wget \
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
####################################################### ANTLR BUILD
FROM openjdk:17-jdk AS antlr-builder
ENV GET_ANTLR_URL https://www.antlr.org/download
ENV ANTLR_VERSION 4.9.3

WORKDIR /usr/local/lib

RUN set -ex; \
        curl -O \
            "$GET_ANTLR_URL/antlr-$ANTLR_VERSION-complete.jar";

# BUILD FORMATTER
WORKDIR /usr/src/formatter
COPY /api_v3/formatter/formatter.g4 ./
COPY /api_v3/formatter/formatter.java ./

RUN set -ex; \
    cp /usr/local/lib/antlr-4.9.3-complete.jar ./antlr.jar; \
    export CLASSPATH=".:/usr/local/lib/antlr-$ANTLR_VERSION-complete.jar"; \
    java -jar "/usr/local/lib/antlr-$ANTLR_VERSION-complete.jar" formatter.g4 -visitor -no-listener; \
    javac *.java; \
    jar cvfe formatter.jar formatter  *.class ./antlr.jar;

# BUILD SECTIONER
WORKDIR /usr/src/sectioner
COPY /api_v3/sectioner/sectioner.g4 ./
COPY /api_v3/sectioner/sectioner.java ./

RUN set -ex; \
    cp /usr/local/lib/antlr-4.9.3-complete.jar ./antlr.jar; \
    export CLASSPATH=".:/usr/local/lib/antlr-$ANTLR_VERSION-complete.jar"; \
    java -jar "/usr/local/lib/antlr-$ANTLR_VERSION-complete.jar" sectioner.g4 -visitor -no-listener; \
    javac *.java; \
    jar cvfe sectioner.jar sectioner  *.class ./antlr.jar;

####################################################### RELEASE
FROM python:3.10-alpine AS release  
LABEL maintainer courseproduction@bcit.ca

ENV PYTHONUNBUFFERED 1
ENV PATH /code:/opt/venv/bin:$PATH

WORKDIR /code

RUN apk --update add \
        nginx \
        openjdk17 \
        bash; \
    chmod -R 755 /var/lib/nginx;

COPY /nginx/nginx.conf /etc/nginx/nginx.conf
COPY .env ./
COPY .secrets .
COPY manage.py supervisord.conf .
COPY docker-entrypoint.sh /usr/local/bin
COPY --from=qcon-api-base /usr/bin/pandoc /usr/local/bin
COPY --from=qcon-api-base /root/.cache /root/.cache
COPY --from=qcon-api-base /opt/venv /opt/venv

COPY --from=antlr-builder /usr/src/formatter /formatter/jarfile
COPY --from=antlr-builder /usr/src/sectioner /sectioner/jarfile

COPY qcon qcon
COPY api_v2 api_v2
COPY api_v3 api_v3

ENTRYPOINT ["docker-entrypoint.sh"]

EXPOSE 8000
CMD ["supervisord", "-c", "supervisord.conf", "-n"]