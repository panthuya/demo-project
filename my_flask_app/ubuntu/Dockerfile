FROM ubuntu:latest
RUN apt update -y \
    && apt install --no-install-recommends --no-install-suggests -y curl \
    && rm -rf /var/lib/apt/lists/*
ENV SITE_URL=http://google.com
WORKDIR  /data
VOLUME  /data
CMD ["sh", "-c", "curl -Lk $SITE_URL > /data/results.txt"]