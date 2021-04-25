FROM nginxinc/nginx-unprivileged:1-alpine

COPY ./default.conf /etc/nginx/conf.d/default.conf
COPY ./uwsgi_params /etc/nginx/uwsgi_params

# root user
USER root

# make folder
RUN mkdir -p /vol/static

# grant all access
RUN chmod 755 /vol/static

USER nginx
