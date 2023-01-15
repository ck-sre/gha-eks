FROM python:3.9
ENV POETRY_VERSION=1.1.8
RUN pip install "poetry==$POETRY_VERSION"
WORKDIR /app
COPY .env .
COPY app-src .
RUN ls -lrth
RUN poetry install
EXPOSE 8000
ENTRYPOINT ["./docker-entrypoint.sh"]
