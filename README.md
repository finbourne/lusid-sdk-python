# LUSID<sup>®</sup> C# SDK

The PyPi package for the LUSID SDK can installed using the following:

```
$ pip install lusid-sdk
```

A pre-generated version of the latest SDK is included in the sdk folder based on the OpenAPI specification named lusid.json in the root folder. The most up to date version of the OpenAPI specification can be downloaded from https://api.lusid.com/swagger/v0/swagger.json

In addition to the SDK, a set of examples on how to use the SDK can be found in the sdk/tests folder. These exist in the form of unit tests and examples. Further instructions on running them can be found in the README.md file in the SDK folder.

# Generating the SDK

If you would prefer to generate the Python SDK locally from the FINBOURNE OpenAPI specification, follow these steps:
  * download the latest swagger.json file from https://api.lusid.com/swagger/index.html
  * save it in this directory as `lusid.json`
  * run `docker-compose up && docker-compose rm -f`