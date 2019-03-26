#!/bin/bash -e

if [[ ${#1} -eq 0 ]]; then
    echo
    echo "[ERROR] swagger file not specified"
    exit 1
fi

gen_root=/usr/swagger
sdk_output_folder=$gen_root/sdk

#   remove all previously generated files
shopt -s extglob 
echo "removing previous sdk:"
rm -rf $sdk_output_folder/lusid
rm !(*.sln|*.jar|Dockerfile|docker-compose.yml)
shopt -u extglob 

# ignore files
mkdir -p $sdk_output_folder
cp /usr/src/.openapi-generator-ignore $sdk_output_folder

echo "generating sdk"

# generate the SDK
java -jar openapi-generator-cli.jar generate \
    -i $gen_root/$1 \
    -l python \
    -o $sdk_output_folder \
    -c $gen_root/config.json
    
rm -rf $sdk_output_folder/.openapi-generator
rm $sdk_output_folder/.openapi-generator-ignore