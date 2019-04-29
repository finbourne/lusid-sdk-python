FROM maven:3.5-jdk-10

RUN apt-get update && apt-get -y install jq

RUN mkdir -p /usr/src/
WORKDIR /usr/src/

RUN wget http://central.maven.org/maven2/org/openapitools/openapi-generator-cli/4.0.0-beta3/openapi-generator-cli-4.0.0-beta3.jar -O openapi-generator-cli.jar

ADD generate.sh /usr/src/
ADD .openapi-generator-ignore /usr/src/

ENTRYPOINT [ "/bin/bash", "generate.sh" ]