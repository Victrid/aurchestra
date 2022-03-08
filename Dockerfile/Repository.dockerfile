FROM python:3.10.2-alpine 
ARG REPOSITORY_VERSION
WORKDIR /data/app
COPY ./repository ./
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.sjtug.sjtu.edu.cn/g' /etc/apk/repositories \
 && apk --no-cache add curl nginx gpg gpg-agent py3-psycopg2 libarchive-tools coreutils \
 && pip install -i https://mirror.sjtu.edu.cn/pypi/web/simple --no-cache-dir -r requirements.txt \
 && mkdir /var/www/aurchestra \
 && mv nginx-host.conf /etc/nginx/http.d/default.conf \
 && mv nginx.conf /etc/nginx/nginx.conf
ENTRYPOINT ./entry.sh
VOLUME ["/var/www/aurchestra"]
EXPOSE 80

