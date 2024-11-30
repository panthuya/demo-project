FROM python:3.10-slim

WORKDIR /app

COPY app-env.py /app

RUN pip install --no-cache-dir Flask

ARG PORT
ENV port=${PORT:-5001}

ARG NAME
ENV NAME=${NAME}

EXPOSE ${port}

CMD ["python", "app-env.py"]