FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /bsoft
WORKDIR /bsoft
COPY requirements.txt /bsoft/
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /bsoft/