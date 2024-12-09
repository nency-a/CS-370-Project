FROM python:3.9

WORKDIR /project

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . /project/

EXPOSE 8000
