FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONNUNBUFFERED 1
ENV DEBUG=True
ENV HOST=0.0.0.0
ENV PORT=8050

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .