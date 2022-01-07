FROM python:3.9 AS qcon-api-base

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
FROM openjdk:19-jdk AS antlr-builder
ENV GET_ANTLR_URL https://www.antlr.org/download
ENV ANTLR_VERSION 4.9.3

WORKDIR /usr/local/lib

RUN set -ex; \
        curl -O \
            "$GET_ANTLR_URL/antlr-$ANTLR_VERSION-complete.jar";

# BUILD FORMATTER
WORKDIR /usr/src/formatter
COPY /api_v3/formatter/formatter.g4 ./

RUN set -ex; \
    export CLASSPATH=".:/usr/local/lib/antlr-$ANTLR_VERSION-complete.jar"; \
    java -jar "/usr/local/lib/antlr-$ANTLR_VERSION-complete.jar" formatter.g4; \
    javac *.java;

# BELOW CODE TEMPLATE FOR OTHER STAGES

# BUILD SPLITTER
# WORKDIR /usr/src/splitter
# COPY /api_v3/splitter/splitter.g4 ./

# RUN set -ex; \
#     export CLASSPATH=".:/usr/local/lib/antlr-$ANTLR_VERSION-complete.jar"; \
#     java -jar "/usr/local/lib/antlr-$ANTLR_VERSION-complete.jar" splitter.g4; \
#     javac *.java;

# # BUILD PARSER
# WORKDIR /usr/src/parser
# COPY /api_v3/parser/parser.g4 ./

# RUN set -ex; \
#     export CLASSPATH=".:/usr/local/lib/antlr-$ANTLR_VERSION-complete.jar"; \
#     java -jar "/usr/local/lib/antlr-$ANTLR_VERSION-complete.jar" parser.g4; \
#     javac *.java;

####################################################### RELEASE
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
COPY .env ./
COPY .secrets .
COPY manage.py supervisord.conf .
COPY docker-entrypoint.sh /usr/local/bin
COPY --from=qcon-api-base /usr/bin/pandoc /usr/local/bin
COPY --from=qcon-api-base /root/.cache /root/.cache
COPY --from=qcon-api-base /opt/venv /opt/venv

COPY --from=antlr-builder /usr/src/formatter /test/formatter

COPY qcon qcon
COPY api_v2 api_v2
COPY api_v3 api_v3

ENTRYPOINT ["docker-entrypoint.sh"]

EXPOSE 8000
CMD ["supervisord", "-c", "supervisord.conf", "-n"]