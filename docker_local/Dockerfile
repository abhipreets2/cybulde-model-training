FROM python:3.10-slim

ARG MLFLOW_ARTIFACT_STORE
ARG MLFLOW_BACKEND_STORE
ENV \
    PYTHONUNBUFFERED=1 \
    VIRTUAL_ENV="${HOME}/venv" \
    PATH="${HOME}/venv/bin:${PATH}" \
    DEBIAN_FRONTEND='noniteractive'

RUN apt-get -qq update \
    && apt-get -qq -y install git \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get -qq -y clean

RUN mkdir -p "${MLFLOW_BACKEND_STORE}" /app
COPY ./docker_local/scripts/run-server.sh /

RUN chmod +x /run-server.sh

RUN HOME=/tmp pip install --no-cache-dir poetry==1.5.1

COPY ./docker_local/pyproject.toml ./docker_local/*.lock /app/
WORKDIR /app

RUN python3.10 -m venv "${VIRTUAL_ENV}" \
	&& pip install --upgrade pip \
	&& poetry install 

CMD ["/run-server.sh"]
