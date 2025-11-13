# lusid.RelationalDatasetsApi

All URIs are relative to *https://fbn-prd.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_upsert_relational_data**](RelationalDatasetsApi.md#batch_upsert_relational_data) | **POST** /api/relationaldatasets/{relationalDatasetDefinitionScope}/{relationalDatasetDefinitionCode}/$batchUpsert | [EXPERIMENTAL] BatchUpsertRelationalData: Batch Upsert Relational Data Points for a given Relational Dataset Definition.
[**query_relational_data**](RelationalDatasetsApi.md#query_relational_data) | **POST** /api/relationaldatasets/{relationalDatasetDefinitionScope}/{relationalDatasetDefinitionCode}/$query | [EXPERIMENTAL] QueryRelationalData: Query Relational Data Points for a given Relational Dataset Definition.


# **batch_upsert_relational_data**
> BatchUpsertRelationalDatasetsResponse batch_upsert_relational_data(relational_dataset_definition_scope, relational_dataset_definition_code, request_body, success_mode=success_mode)

[EXPERIMENTAL] BatchUpsertRelationalData: Batch Upsert Relational Data Points for a given Relational Dataset Definition.

Batch Upsert Relational Data Points for a given Relational Dataset Definition.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    RelationalDatasetsApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "lusidUrl":"https://<your-domain>.lusid.com/api",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the lusid SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(RelationalDatasetsApi)
    relational_dataset_definition_scope = 'relational_dataset_definition_scope_example' # str | The Scope of the relational dataset definition.
    relational_dataset_definition_code = 'relational_dataset_definition_code_example' # str | The Code of the relational dataset definition.
    request_body = {"point1":{"dataPointDataSeries":{"seriesScope":"SeriesScope","applicableEntity":{"entityType":"Instrument","entityScope":"InstrumentScope","identifierScope":"default","identifierType":"default","identifierValue":"IdentifierValue"},"seriesIdentifiers":{"instrumentId":"SomeValue"}},"effectiveAt":"2019-01-01T12:00:00.0000000+00:00","valueFields":{"price":100},"metaDataFields":{"currency":"USD"}},"point2":{"dataPointDataSeries":{"seriesScope":"SeriesScope","applicableEntity":{"entityType":"Instrument"},"seriesIdentifiers":{"instrumentId":"SomeValue"}},"effectiveAt":"2019-01-02T12:00:00.0000000+00:00","valueFields":{"price":200},"metaDataFields":{"currency":"GBP"}},"point3":{"dataPointDataSeries":{"seriesScope":"SeriesScope","applicableEntity":{"entityType":"LegalEntity","entityScope":"LegalEntityScope","identifierScope":"default","identifierType":"default","identifierValue":"IdentifierValue"},"seriesIdentifiers":{"instrumentId":"OtherValue"}},"effectiveAt":"2019-01-01T12:00:00.0000000+00:00","valueFields":{"price":250},"metaDataFields":{"currency":"EUR"}}} # Dict[str, UpsertRelationalDataPointRequest] | The DataPoints to upsert.
    success_mode = 'Partial' # str | Whether the batch request should fail Atomically or in a Partial fashion - Allowed Values: Atomic, Partial.              Note: If using partial failure modes, then it is important to check the response body for failures as any failures will still return a 200 status code. (optional) (default to 'Partial')

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.batch_upsert_relational_data(relational_dataset_definition_scope, relational_dataset_definition_code, request_body, success_mode=success_mode, opts=opts)

        # [EXPERIMENTAL] BatchUpsertRelationalData: Batch Upsert Relational Data Points for a given Relational Dataset Definition.
        api_response = api_instance.batch_upsert_relational_data(relational_dataset_definition_scope, relational_dataset_definition_code, request_body, success_mode=success_mode)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling RelationalDatasetsApi->batch_upsert_relational_data: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **relational_dataset_definition_scope** | **str**| The Scope of the relational dataset definition. | 
 **relational_dataset_definition_code** | **str**| The Code of the relational dataset definition. | 
 **request_body** | [**Dict[str, UpsertRelationalDataPointRequest]**](UpsertRelationalDataPointRequest.md)| The DataPoints to upsert. | 
 **success_mode** | **str**| Whether the batch request should fail Atomically or in a Partial fashion - Allowed Values: Atomic, Partial.              Note: If using partial failure modes, then it is important to check the response body for failures as any failures will still return a 200 status code. | [optional] [default to &#39;Partial&#39;]

### Return type

[**BatchUpsertRelationalDatasetsResponse**](BatchUpsertRelationalDatasetsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The relational data points that were upserted. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **query_relational_data**
> PagedResourceListOfRelationalDataPointResponse query_relational_data(relational_dataset_definition_scope, relational_dataset_definition_code, as_at=as_at, effective_at=effective_at, page=page, limit=limit, query_relational_dataset_request=query_relational_dataset_request)

[EXPERIMENTAL] QueryRelationalData: Query Relational Data Points for a given Relational Dataset Definition.

Query Relational Data Points for a given Relational Dataset Definition.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    RelationalDatasetsApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "lusidUrl":"https://<your-domain>.lusid.com/api",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the lusid SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(RelationalDatasetsApi)
    relational_dataset_definition_scope = 'relational_dataset_definition_scope_example' # str | The Scope of the relational dataset definition.
    relational_dataset_definition_code = 'relational_dataset_definition_code_example' # str | The Code of the relational dataset definition.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the dataset(s). Defaults to returning the latest version of each dataset if not specified. (optional)
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to query the datasets.              Defaults to the current LUSID system datetime if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue query datasets. This value is returned from the previous call.              If a pagination token is provided, the filter, customSortBy, effectiveAt and asAt fields must not have changed since the original request. (optional)
    limit = 56 # int | When paginating, limit the results to this number. Defaults to 100 if not specified. (optional)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # query_relational_dataset_request = QueryRelationalDatasetRequest.from_json("")
    # query_relational_dataset_request = QueryRelationalDatasetRequest.from_dict({})
    query_relational_dataset_request = QueryRelationalDatasetRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.query_relational_data(relational_dataset_definition_scope, relational_dataset_definition_code, as_at=as_at, effective_at=effective_at, page=page, limit=limit, query_relational_dataset_request=query_relational_dataset_request, opts=opts)

        # [EXPERIMENTAL] QueryRelationalData: Query Relational Data Points for a given Relational Dataset Definition.
        api_response = api_instance.query_relational_data(relational_dataset_definition_scope, relational_dataset_definition_code, as_at=as_at, effective_at=effective_at, page=page, limit=limit, query_relational_dataset_request=query_relational_dataset_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling RelationalDatasetsApi->query_relational_data: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **relational_dataset_definition_scope** | **str**| The Scope of the relational dataset definition. | 
 **relational_dataset_definition_code** | **str**| The Code of the relational dataset definition. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the dataset(s). Defaults to returning the latest version of each dataset if not specified. | [optional] 
 **effective_at** | **str**| The effective datetime or cut label at which to query the datasets.              Defaults to the current LUSID system datetime if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue query datasets. This value is returned from the previous call.              If a pagination token is provided, the filter, customSortBy, effectiveAt and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **query_relational_dataset_request** | [**QueryRelationalDatasetRequest**](QueryRelationalDatasetRequest.md)| The query request. | [optional] 

### Return type

[**PagedResourceListOfRelationalDataPointResponse**](PagedResourceListOfRelationalDataPointResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The relational data points that were queried. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

