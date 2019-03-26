#!/bin/bash

# get the specificed swagger file
curl -L https://api-am-ci.lusid.com/swagger/v0/swagger.json -o lusid.json

#   build the sdk
docker-compose build && docker-compose up && docker-compose rm -f