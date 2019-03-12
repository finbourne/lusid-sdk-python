FROM 707585552459.dkr.ecr.eu-west-1.amazonaws.com/dotnetcoresdk-awscli

RUN mkdir -p /usr/src/
RUN mkdir -p /usr/work/
WORKDIR /usr/src/

ADD publish.sh /usr/work

ENTRYPOINT [ "/bin/bash", "/usr/work/publish.sh"]