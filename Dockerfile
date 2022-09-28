# Dockerfile

## Base
FROM registry.dev.ltc.bcit.ca/ltc-infrastructure/images/qcon-api-base AS qcon-api-base

RUN set -ex; \
        pip install celery \
        pip install redis \ 
        pip install channels_redis \
        pip install JSON-log-formatter \
        pip install psycopg2-binary \
        pip install elastic-apm

## ANLR Builder
FROM openjdk:17-jdk AS antlr-builder

ENV GET_ANTLR_URL https://www.antlr.org/download
ENV ANTLR_VERSION 4.9.3

WORKDIR /usr/local/lib

RUN set -ex; \
        curl -O \
            "$GET_ANTLR_URL/antlr-$ANTLR_VERSION-complete.jar";

### Build Formatter
WORKDIR /usr/src/formatter

COPY /api_v3/formatter/formatter.g4 ./
COPY /api_v3/formatter/formatter.java ./

RUN set -ex; \
    cp /usr/local/lib/antlr-4.9.3-complete.jar ./antlr.jar; \
    export CLASSPATH=".:/usr/local/lib/antlr-$ANTLR_VERSION-complete.jar"; \
    java -jar "/usr/local/lib/antlr-$ANTLR_VERSION-complete.jar" formatter.g4 -visitor -no-listener; \
    javac *.java; \
    jar cvfe formatter.jar formatter  *.class ./antlr.jar;

### Build Sectioner
WORKDIR /usr/src/sectioner

COPY /api_v3/sectioner/sectioner.g4 ./
COPY /api_v3/sectioner/sectioner.java ./

RUN set -ex; \
    cp /usr/local/lib/antlr-4.9.3-complete.jar ./antlr.jar; \
    export CLASSPATH=".:/usr/local/lib/antlr-$ANTLR_VERSION-complete.jar"; \
    java -jar "/usr/local/lib/antlr-$ANTLR_VERSION-complete.jar" sectioner.g4 -visitor -no-listener; \
    javac *.java; \
    jar cvfe sectioner.jar sectioner  *.class ./antlr.jar;

### Build Splitter
WORKDIR /usr/src/splitter

COPY /api_v3/splitter/splitter.g4 ./
COPY /api_v3/splitter/splitter.java ./

RUN set -ex; \
    cp /usr/local/lib/antlr-4.9.3-complete.jar ./antlr.jar; \
    export CLASSPATH=".:/usr/local/lib/antlr-$ANTLR_VERSION-complete.jar"; \
    java -jar "/usr/local/lib/antlr-$ANTLR_VERSION-complete.jar" splitter.g4 -visitor -no-listener; \
    javac *.java; \
    jar cvfe splitter.jar splitter  *.class ./antlr.jar;

### Build Questionparser
WORKDIR /usr/src/questionparser

COPY /api_v3/questionparser/questionparser.g4 ./
COPY /api_v3/questionparser/questionparser.java ./

RUN set -ex; \
    cp /usr/local/lib/antlr-4.9.3-complete.jar ./antlr.jar; \
    export CLASSPATH=".:/usr/local/lib/antlr-$ANTLR_VERSION-complete.jar"; \
    java -jar "/usr/local/lib/antlr-$ANTLR_VERSION-complete.jar" questionparser.g4 -visitor -no-listener; \
    javac *.java; \
    jar cvfe questionparser.jar questionparser  *.class ./antlr.jar;

### Build Endanswers
WORKDIR /usr/src/endanswers

COPY /api_v3/endanswers/endanswers.g4 ./
COPY /api_v3/endanswers/endanswers.java ./

RUN set -ex; \
    cp /usr/local/lib/antlr-4.9.3-complete.jar ./antlr.jar; \
    export CLASSPATH=".:/usr/local/lib/antlr-$ANTLR_VERSION-complete.jar"; \
    java -jar "/usr/local/lib/antlr-$ANTLR_VERSION-complete.jar" endanswers.g4 -visitor -no-listener; \
    javac *.java; \
    jar cvfe endanswers.jar endanswers  *.class ./antlr.jar;


## Release
# FROM python:3.10-alpine AS release
FROM python:slim AS release

LABEL maintainer courseproduction@bcit.ca

ENV PYTHONUNBUFFERED 1
ENV PATH /code:/opt/venv/bin:$PATH

WORKDIR /code

RUN set -ex; \
        apt-get update; \
        apt-get install -y --no-install-recommends \
            redis \
            openjdk-17-jdk-headless; \
        mkdir -p /run/daphne;

COPY .env ./
COPY manage.py supervisord.conf ./
COPY docker-entrypoint.sh /usr/local/bin

COPY --from=qcon-api-base /usr/bin/pandoc /usr/local/bin
COPY --from=qcon-api-base /root/.cache /root/.cache
COPY --from=qcon-api-base /opt/venv /opt/venv

COPY --from=antlr-builder /usr/src/formatter /formatter/jarfile
COPY --from=antlr-builder /usr/src/sectioner /sectioner/jarfile
COPY --from=antlr-builder /usr/src/splitter /splitter/jarfile
COPY --from=antlr-builder /usr/src/questionparser /questionparser/jarfile
COPY --from=antlr-builder /usr/src/endanswers /endanswers/jarfile

COPY qcon qcon
COPY api_v2 api_v2
COPY api_v3 api_v3

ENTRYPOINT ["docker-entrypoint.sh"]

EXPOSE 8001
CMD ["supervisord", "-c", "supervisord.conf", "-n"]
