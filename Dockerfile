# Dockerfile

## Base
FROM registry.dev.ltc.bcit.ca/ltc-infrastructure/images/qcon-api-base AS qcon-api-base

ENV ANTLR_VERSION 4.11.0
ENV ANTLR_HOME /root/.m2/repository/org/antlr/antlr4/
ENV CLASSPATH=$CLASSPATH:$ANTLR_HOME/$ANTLR_VERSION/antlr4-$ANTLR_VERSION-complete.jar

RUN set -ex; \
        pip install jaro-winkler; \
        pip install antlr4-tools;

RUN set -ex; \
        apt-get update; \
        apt-get install -y --no-install-recommends \
                openjdk-17-jdk \
                openjdk-17-jre; \
        antlr4 -v $ANTLR_VERSION;

### Build Formatter
WORKDIR /usr/src/formatter
COPY /api/antlr/formatter/formatter.g4 /api/antlr/formatter/formatter.java ./
RUN set -ex; \
        cp $ANTLR_HOME/$ANTLR_VERSION/antlr4-$ANTLR_VERSION-complete.jar ./antlr.jar; \
        antlr4 -v $ANTLR_VERSION formatter.g4 -visitor -no-listener; \
        javac *.java; \
        jar cvfe formatter.jar formatter  *.class ./antlr.jar;
### Build Sectioner
WORKDIR /usr/src/sectioner
COPY /api/antlr/sectioner/sectioner.g4 /api/antlr/sectioner/sectioner.java ./
RUN set -ex; \
        cp $ANTLR_HOME/$ANTLR_VERSION/antlr4-$ANTLR_VERSION-complete.jar ./antlr.jar; \
        antlr4 -v $ANTLR_VERSION sectioner.g4 -visitor -no-listener; \
        javac *.java; \
        jar cvfe sectioner.jar sectioner  *.class ./antlr.jar;
### Build Splitter
WORKDIR /usr/src/splitter
COPY /api/antlr/splitter/splitter.g4 /api/antlr/splitter/splitter.java ./
RUN set -ex; \
        cp $ANTLR_HOME/$ANTLR_VERSION/antlr4-$ANTLR_VERSION-complete.jar ./antlr.jar; \
        antlr4 -v $ANTLR_VERSION splitter.g4 -visitor -no-listener; \
        javac *.java; \
        jar cvfe splitter.jar splitter  *.class ./antlr.jar;
### Build Questionparser
WORKDIR /usr/src/questionparser
COPY /api/antlr/questionparser/questionparser.g4 /api/antlr/questionparser/questionparser.java ./
RUN set -ex; \
        cp $ANTLR_HOME/$ANTLR_VERSION/antlr4-$ANTLR_VERSION-complete.jar ./antlr.jar; \
        antlr4 -v $ANTLR_VERSION questionparser.g4 -visitor -no-listener; \
        javac *.java; \
        jar cvfe questionparser.jar questionparser  *.class ./antlr.jar;
### Build Endanswers
WORKDIR /usr/src/endanswers
COPY /api/antlr/endanswers/endanswers.g4 /api/antlr/endanswers/endanswers.java ./
RUN set -ex; \
        cp $ANTLR_HOME/$ANTLR_VERSION/antlr4-$ANTLR_VERSION-complete.jar ./antlr.jar; \
        antlr4 -v $ANTLR_VERSION endanswers.g4 -visitor -no-listener; \
        javac *.java; \
        jar cvfe endanswers.jar endanswers  *.class ./antlr.jar;

## Release
# FROM python:3.10-alpine AS release
FROM python:3.11-slim AS release

LABEL maintainer courseproduction@bcit.ca

ENV PYTHONUNBUFFERED 1
ENV PATH /code:/opt/venv/bin:$PATH

WORKDIR /code

RUN set -ex; \
        apt-get update; \
        apt-get install -y --no-install-recommends \
            redis \
            libreoffice-writer \
            openjdk-17-jdk-headless; \
        mkdir -p /run/daphne;

COPY .env manage.py ./
COPY docker-entrypoint.sh /usr/local/bin

COPY --from=qcon-api-base /usr/bin/pandoc /usr/local/bin
COPY --from=qcon-api-base /root/.cache /root/.cache
COPY --from=qcon-api-base /opt/venv /opt/venv

COPY --from=qcon-api-base /usr/src /antlr_build

COPY qcon qcon
COPY api api

ENTRYPOINT ["docker-entrypoint.sh"]

EXPOSE 8000
CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "qcon.asgi:application"]
