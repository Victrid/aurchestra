FROM alpine:3.15
ENV NODE_VERSION 16.14.0
WORKDIR /data/app
ARG REPOSITORY_VERSION

USER root
RUN apk update && apk add bash
RUN apk add --update npm
RUN node -v
RUN npm -v

RUN npm config rm proxy
RUN npm config rm https-proxy --tried removing npm proxy
RUN npm uninstall uuid
RUN npm install uuid@7.0.3
RUN npm install pm2@latest -g
# Bundle APP files
COPY ./ ./
# COPY package.json .
# COPY pm2.json .

# # Install app dependencies
ENV NPM_CONFIG_LOGLEVEL warn
RUN npm install --production
# Show current folder structure in logs
RUN ls -al -R
RUN ["chmod", "+x", "/data/app/docker-entrypoint.sh"]
RUN npm run build

ENTRYPOINT ./docker-entrypoint.sh

EXPOSE 3000