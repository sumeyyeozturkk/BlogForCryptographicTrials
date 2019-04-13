FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /blog
WORKDIR /blog
COPY . /blog/
RUN pip install -r requirements.txt
