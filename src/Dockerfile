FROM python:3.9.0-alpine as base

FROM base as builder

RUN mkdir /install
WORKDIR /install

COPY requirements.txt /requirements.txt
RUN pip install --prefix=/install -r /requirements.txt

FROM base

COPY --from=builder /install /usr/local
COPY . /app/

WORKDIR /app

ENTRYPOINT ["./pytaskr"]
