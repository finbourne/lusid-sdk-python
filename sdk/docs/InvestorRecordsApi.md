# lusid.InvestorRecordsApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_investor_record**](InvestorRecordsApi.md#delete_investor_record) | **DELETE** /api/investorrecords/{idTypeScope}/{idTypeCode}/{code} | DeleteInvestorRecord: Delete Investor Record
[**get_investor_record**](InvestorRecordsApi.md#get_investor_record) | **GET** /api/investorrecords/{idTypeScope}/{idTypeCode}/{code} | [EARLY ACCESS] GetInvestorRecord: Get Investor Record
[**upsert_investor_records**](InvestorRecordsApi.md#upsert_investor_records) | **POST** /api/investorrecords/$batchUpsert | [EARLY ACCESS] UpsertInvestorRecords: Pluralised upsert of Investor Records


# **delete_investor_record**
> DeletedEntityResponse delete_investor_record(id_type_scope, id_type_code, code)

DeleteInvestorRecord: Delete Investor Record

Delete an investor record. Deletion will be valid from the investor record's creation datetime.  This means that the investor record will no longer exist at any effective datetime from the asAt datetime of deletion.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    InvestorRecordsApi
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
    api_instance = api_client_factory.build(InvestorRecordsApi)
    id_type_scope = 'id_type_scope_example' # str | The scope of the investor record identifier type.
    id_type_code = 'id_type_code_example' # str | The code of the investor record identifier type.
    code = 'code_example' # str | Code of the investor record under specified identifier type's scope and code. This together with defined              identifier type uniquely identifies the investor record to delete.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_investor_record(id_type_scope, id_type_code, code, opts=opts)

        # DeleteInvestorRecord: Delete Investor Record
        api_response = api_instance.delete_investor_record(id_type_scope, id_type_code, code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling InvestorRecordsApi->delete_investor_record: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_type_scope** | **str**| The scope of the investor record identifier type. | 
 **id_type_code** | **str**| The code of the investor record identifier type. | 
 **code** | **str**| Code of the investor record under specified identifier type&#39;s scope and code. This together with defined              identifier type uniquely identifies the investor record to delete. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response from deleting investor record. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_investor_record**
> InvestorRecord get_investor_record(id_type_scope, id_type_code, code, property_keys=property_keys, effective_at=effective_at, as_at=as_at, relationship_definition_ids=relationship_definition_ids)

[EARLY ACCESS] GetInvestorRecord: Get Investor Record

Retrieve the definition of a investor record.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    InvestorRecordsApi
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
    api_instance = api_client_factory.build(InvestorRecordsApi)
    id_type_scope = 'id_type_scope_example' # str | Scope of the investor record identifier type.
    id_type_code = 'id_type_code_example' # str | Code of the investor record identifier type.
    code = 'code_example' # str | Code of the investor record under specified identifier type's scope and code. This together with stated identifier type uniquely              identifies the investor record.
    property_keys = ['property_keys_example'] # List[str] | A list of property keys or identifier types (as property keys) from the \"InvestorRecord\" domain              to include for found investor record, or from any domain that supports relationships to decorate onto related entities.              These take the format {domain}/{scope}/{code} e.g. \"InvestorRecord/ContactDetails/Address\". (optional)
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the investor record. Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the investor record. Defaults to return the latest version of the investor record if not specified. (optional)
    relationship_definition_ids = ['relationship_definition_ids_example'] # List[str] | A list of relationship definitions that are used to decorate related entities              onto the investor record in the response. These must take the form {relationshipDefinitionScope}/{relationshipDefinitionCode}. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_investor_record(id_type_scope, id_type_code, code, property_keys=property_keys, effective_at=effective_at, as_at=as_at, relationship_definition_ids=relationship_definition_ids, opts=opts)

        # [EARLY ACCESS] GetInvestorRecord: Get Investor Record
        api_response = api_instance.get_investor_record(id_type_scope, id_type_code, code, property_keys=property_keys, effective_at=effective_at, as_at=as_at, relationship_definition_ids=relationship_definition_ids)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling InvestorRecordsApi->get_investor_record: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_type_scope** | **str**| Scope of the investor record identifier type. | 
 **id_type_code** | **str**| Code of the investor record identifier type. | 
 **code** | **str**| Code of the investor record under specified identifier type&#39;s scope and code. This together with stated identifier type uniquely              identifies the investor record. | 
 **property_keys** | [**List[str]**](str.md)| A list of property keys or identifier types (as property keys) from the \&quot;InvestorRecord\&quot; domain              to include for found investor record, or from any domain that supports relationships to decorate onto related entities.              These take the format {domain}/{scope}/{code} e.g. \&quot;InvestorRecord/ContactDetails/Address\&quot;. | [optional] 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the investor record. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the investor record. Defaults to return the latest version of the investor record if not specified. | [optional] 
 **relationship_definition_ids** | [**List[str]**](str.md)| A list of relationship definitions that are used to decorate related entities              onto the investor record in the response. These must take the form {relationshipDefinitionScope}/{relationshipDefinitionCode}. | [optional] 

### Return type

[**InvestorRecord**](InvestorRecord.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested investor record |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **upsert_investor_records**
> UpsertInvestorRecordsResponse upsert_investor_records(success_mode, request_body)

[EARLY ACCESS] UpsertInvestorRecords: Pluralised upsert of Investor Records

Creates or updates a collection of Investor Records

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    InvestorRecordsApi
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
    api_instance = api_client_factory.build(InvestorRecordsApi)
    success_mode = 'success_mode_example' # str | Whether the batch request should fail Atomically or in a Partial fashion - Allowed Values: Atomic, Partial
    request_body = {"firstExampleRequest":{"identifiers":{"InvestorRecord/ExternalIdentifier/ExternalIRId":{"key":"InvestorRecord/ExternalIdentifier/ExternalIRId","value":{"labelValue":"IR_12345678"}},"InvestorRecord/InternalIdentifier/InternalIRId":{"key":"InvestorRecord/InternalIdentifier/InternalIRId","value":{"labelValue":"Internal_XHSP2038"}}},"properties":{"InvestorRecord/Details/Name":{"key":"InvestorRecord/Details/Name","value":{"labelValue":"John Doe"}},"InvestorRecord/Details/Country":{"key":"InvestorRecord/Details/Country","value":{"labelValue":"United Kingdom"},"effectiveFrom":"2016-01-01T00:00:00.0000000+00:00"}},"displayName":"InvestorRecord1DisplayName","description":"InvestorRecord1Description","investor":{"investorType":"Person","investorIdentifiers":{"Person/HrSystem1/InternalId":{"key":"Person/HrSystem1/InternalId","value":{"labelValue":"XY10001111"}}}}},"secondExampleRequest":{"identifiers":{"InvestorRecord/ExternalIdentifier/ExternalIRId":{"key":"InvestorRecord/ExternalIdentifier/ExternalIRId","value":{"labelValue":"IR_22345678"}},"InvestorRecord/InternalIdentifier/InternalIRId":{"key":"InvestorRecord/InternalIdentifier/InternalIRId","value":{"labelValue":"Internal_XHSP2039"}}},"properties":{"InvestorRecord/Details/Name":{"key":"InvestorRecord/Details/Name","value":{"labelValue":"Jane Doe"}},"InvestorRecord/Details/Country":{"key":"InvestorRecord/Details/Country","value":{"labelValue":"Germany"},"effectiveFrom":"2016-01-01T00:00:00.0000000+00:00"}},"displayName":"InvestorRecord2DisplayName","description":"InvestorRecord2Description","investor":{"investorType":"LegalEntity","investorIdentifiers":{"LegalEntity/ExternalIdentifier/LEI":{"key":"LegalEntity/ExternalIdentifier/LEI","value":{"labelValue":"LEI_12345678"}}}}}} # Dict[str, UpsertInvestorRecordRequest] | A collection of requests to create or update Investor Records.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.upsert_investor_records(success_mode, request_body, opts=opts)

        # [EARLY ACCESS] UpsertInvestorRecords: Pluralised upsert of Investor Records
        api_response = api_instance.upsert_investor_records(success_mode, request_body)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling InvestorRecordsApi->upsert_investor_records: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **success_mode** | **str**| Whether the batch request should fail Atomically or in a Partial fashion - Allowed Values: Atomic, Partial | 
 **request_body** | [**Dict[str, UpsertInvestorRecordRequest]**](UpsertInvestorRecordRequest.md)| A collection of requests to create or update Investor Records. | 

### Return type

[**UpsertInvestorRecordsResponse**](UpsertInvestorRecordsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The successfully created or updated investor records along with any failures |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

