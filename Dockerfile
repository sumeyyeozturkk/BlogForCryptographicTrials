FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /blog
WORKDIR /blog
COPY requirements.txt /blog/
RUN pip install -r requirements.txt
COPY . /blog/
