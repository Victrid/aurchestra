FROM nginx:latest
RUN rm -rf /etc/nginx && mkdir /etc/nginx
COPY ./nginx /etc/nginx
