# pull official base image
FROM python:3.8.3

# set work directory
WORKDIR /root/otp

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt ./
RUN pip install -r requirements.txt

# copy project
COPY . .

COPY ./scripts /scripts

RUN chmod +x /scripts/*

RUN mkdir -p /vol/web/media

RUN mkdir -p /vol/web/static

# RUN adduser -D user
# RUN chown -R user:user /vol
# RUN chmod -R 755 /vol/web
# USER user

# CMD ["sh", "entrypoint.sh"]
