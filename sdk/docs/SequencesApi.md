# lusid.SequencesApi

All URIs are relative to *https://fbn-prd.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sequence**](SequencesApi.md#create_sequence) | **POST** /api/sequences/{scope} | [EARLY ACCESS] CreateSequence: Create a new sequence
[**get_sequence**](SequencesApi.md#get_sequence) | **GET** /api/sequences/{scope}/{code} | [EARLY ACCESS] GetSequence: Get a specified sequence
[**list_sequences**](SequencesApi.md#list_sequences) | **GET** /api/sequences | [EARLY ACCESS] ListSequences: List Sequences
[**next**](SequencesApi.md#next) | **GET** /api/sequences/{scope}/{code}/next | [EARLY ACCESS] Next: Get next values from sequence


# **create_sequence**
> SequenceDefinition create_sequence(scope, create_sequence_request)

[EARLY ACCESS] CreateSequence: Create a new sequence

Create a new sequence

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    SequencesApi
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
    api_instance = api_client_factory.build(SequencesApi)
    scope = 'scope_example' # str | Scope of the sequence.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # create_sequence_request = CreateSequenceRequest.from_json("")
    # create_sequence_request = CreateSequenceRequest.from_dict({})
    create_sequence_request = CreateSequenceRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.create_sequence(scope, create_sequence_request, opts=opts)

        # [EARLY ACCESS] CreateSequence: Create a new sequence
        api_response = api_instance.create_sequence(scope, create_sequence_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling SequencesApi->create_sequence: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of the sequence. | 
 **create_sequence_request** | [**CreateSequenceRequest**](CreateSequenceRequest.md)| Request to create sequence | 

### Return type

[**SequenceDefinition**](SequenceDefinition.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created Sequence |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_sequence**
> SequenceDefinition get_sequence(scope, code)

[EARLY ACCESS] GetSequence: Get a specified sequence

Return the details of a specified sequence

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    SequencesApi
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
    api_instance = api_client_factory.build(SequencesApi)
    scope = 'scope_example' # str | Scope of the sequence.
    code = 'code_example' # str | Code of the sequence. This together with stated scope uniquely             identifies the sequence.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_sequence(scope, code, opts=opts)

        # [EARLY ACCESS] GetSequence: Get a specified sequence
        api_response = api_instance.get_sequence(scope, code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling SequencesApi->get_sequence: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of the sequence. | 
 **code** | **str**| Code of the sequence. This together with stated scope uniquely             identifies the sequence. | 

### Return type

[**SequenceDefinition**](SequenceDefinition.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested sequence |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_sequences**
> PagedResourceListOfSequenceDefinition list_sequences(page=page, limit=limit, filter=filter)

[EARLY ACCESS] ListSequences: List Sequences

List sequences which satisfies filtering criteria.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    SequencesApi
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
    api_instance = api_client_factory.build(SequencesApi)
    page = 'page_example' # str | The pagination token to use to continue listing sequences from a previous call to list sequences. This value is returned from the previous call. (optional)
    limit = 56 # int | When paginating, limit the number of returned results to this many. Defaults to 500 if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the result set.              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_sequences(page=page, limit=limit, filter=filter, opts=opts)

        # [EARLY ACCESS] ListSequences: List Sequences
        api_response = api_instance.list_sequences(page=page, limit=limit, filter=filter)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling SequencesApi->list_sequences: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **str**| The pagination token to use to continue listing sequences from a previous call to list sequences. This value is returned from the previous call. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 500 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set.              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**PagedResourceListOfSequenceDefinition**](PagedResourceListOfSequenceDefinition.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The sequences matching filtering criteria |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **next**
> NextValueInSequenceResponse next(scope, code, batch=batch)

[EARLY ACCESS] Next: Get next values from sequence

Get the next set of values from a specified sequence

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    SequencesApi
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
    api_instance = api_client_factory.build(SequencesApi)
    scope = 'scope_example' # str | Scope of the sequence.
    code = 'code_example' # str | Code of the sequence. This together with stated scope uniquely             identifies the sequence.
    batch = 56 # int | Number of sequences items to return for the specified sequence. Default to 1 if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.next(scope, code, batch=batch, opts=opts)

        # [EARLY ACCESS] Next: Get next values from sequence
        api_response = api_instance.next(scope, code, batch=batch)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling SequencesApi->next: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of the sequence. | 
 **code** | **str**| Code of the sequence. This together with stated scope uniquely             identifies the sequence. | 
 **batch** | **int**| Number of sequences items to return for the specified sequence. Default to 1 if not specified. | [optional] 

### Return type

[**NextValueInSequenceResponse**](NextValueInSequenceResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response containing next available values in specified sequence. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

