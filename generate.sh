#!/bin/bash -e

if [[ ${#1} -eq 0 ]]; then
    echo
    echo "[ERROR] swagger file not specified"
    exit 1
fi

gen_root=/usr/swagger
sdk_output_folder=$gen_root/sdk
swagger_file=$gen_root/$1
config_file=$gen_root/config.json

#   remove all previously generated files
shopt -s extglob 
echo "removing previous sdk: $sdk_output_folder"
rm -rf $sdk_output_folder/lusid
shopt -u extglob 

# ignore files
mkdir -p $sdk_output_folder
cp /usr/src/.openapi-generator-ignore $sdk_output_folder

sdk_version=$(cat $swagger_file | jq -r '.info.version')
cat $config_file | jq -r --arg SDK_VERSION "$sdk_version" '.packageVersion |= $SDK_VERSION' > temp && mv temp $config_file

echo "generating sdk version: $sdk_version"

# generate the SDK
java -jar openapi-generator-cli.jar generate \
    -i $gen_root/$1 \
    -g python \
    -o $sdk_output_folder \
    -c $config_file   

# create a version file
cat << EOF > $sdk_output_folder/lusid/__version__.py
__version__ = "$sdk_version"
EOF

rm -rf $sdk_output_folder/.openapi-generator
rm $sdk_output_folder/.openapi-generator-ignore