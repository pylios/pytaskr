FROM python:3.9.0-alpine
COPY . /app
WORKDIR "/app"
RUN pip install -r ./requirements.txt
ENTRYPOINT ["./pytaskr"]
