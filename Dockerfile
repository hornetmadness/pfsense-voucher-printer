FROM python:3.7-slim

ENV APPDIR /app

USER root

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y python3-psycopg2 curl sqlite3 && \
    apt-get clean  

RUN mkdir $APPDIR
ADD requirements.txt $APPDIR/
RUN pip3 install -r $APPDIR/requirements.txt --no-cache-dir --no-color

ADD . $APPDIR/

EXPOSE 5000

USER nobody

ENTRYPOINT ["/app/start.sh"]
