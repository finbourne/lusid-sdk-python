FROM python:3.7.0

RUN pip install twine

RUN mkdir -p /usr/src/
RUN mkdir -p /usr/work/

WORKDIR /usr/src/sdk

ADD publish.sh /usr/work

ENTRYPOINT [ "/bin/bash", "/usr/work/publish.sh"]