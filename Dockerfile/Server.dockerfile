FROM alpine:3.15
ENV NODE_VERSION 16.14.0
WORKDIR /data/app
ARG REPOSITORY_VERSION

USER root
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.sjtug.sjtu.edu.cn/g' /etc/apk/repositories \
 && apk add --update bash npm \
 && npm set registry https://registry.npmmirror.com \
 && npm uninstall uuid && npm install uuid@7.0.3 \
 && npm install webpack webpack-cli -g 
# Bundle APP files
COPY ./Server ./
# COPY package.json .
# COPY pm2.json .

# # Install app dependencies
ENV NPM_CONFIG_LOGLEVEL warn
ENV PORT=80
RUN npm install --production \
 && npm install webpack pg \
 && npm run build


ENTRYPOINT ./docker-entrypoint.sh
EXPOSE 80
