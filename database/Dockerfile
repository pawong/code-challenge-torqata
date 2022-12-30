from postgres:13.6

ENV POSTGRES_DB torqata
ENV POSTGRES_USER postgres

COPY load-extensions.sh /docker-entrypoint-initdb.d/
COPY init.sql /docker-entrypoint-initdb.d/
