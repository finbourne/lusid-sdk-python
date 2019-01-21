FROM microsoft/dotnet:2.0-sdk

RUN mkdir -p /usr/src
WORKDIR /usr/src

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils && \
    curl -sL https://deb.nodesource.com/setup_8.x | bash - && \
    apt-get install -y nodejs && \
    apt-get install npm

RUN npm install -g autorest@2.0.4283

CMD autorest --python
