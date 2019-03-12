#!/bin/bash 

set -e

if [[ (${#1} -eq 0) ]] ; then
    echo 
    echo "[ERROR] missing API key"
    echo
    exit 1
fi

NUGET_API_KEY=$1
sdk_version=$(cat lusid.json | jq -r '.info.version')

sed -i 's/<Version>.*<\/Version>/<Version>'$sdk_version'<\/Version>/g' sdk/Lusid.Sdk/Lusid.Sdk.csproj

echo "sdk_version=$sdk_version"

dotnet pack -c Release sdk/Lusid.Sdk/Lusid.Sdk.csproj
dotnet nuget push sdk/Lusid.Sdk/bin/Release/Lusid.Sdk.${sdk_version}.nupkg \
    --source https://nuget.org \
    --api-key $NUGET_API_KEY