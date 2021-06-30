# lusid.LegalEntitiesApi

All URIs are relative to *http://local-unit-test-server.lusid.com:47048*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_legal_entity**](LegalEntitiesApi.md#delete_legal_entity) | **DELETE** /api/legalentities/{idTypeScope}/{idTypeCode}/{code} | [EARLY ACCESS] Delete Legal Entity
[**get_legal_entity**](LegalEntitiesApi.md#get_legal_entity) | **GET** /api/legalentities/{idTypeScope}/{idTypeCode}/{code} | [EARLY ACCESS] Get Legal Entity
[**list_legal_entities**](LegalEntitiesApi.md#list_legal_entities) | **GET** /api/legalentities/{idTypeScope}/{idTypeCode} | [EARLY ACCESS] List Legal Entities
[**upsert_legal_entity**](LegalEntitiesApi.md#upsert_legal_entity) | **POST** /api/legalentities | [EARLY ACCESS] Upsert Legal Entity


# **delete_legal_entity**
> DeletedEntityResponse delete_legal_entity(id_type_scope, id_type_code, code)

[EARLY ACCESS] Delete Legal Entity

Delete a legal entity. Deletion will be valid from the legal entity's creation datetime.  This means that the legal entity will no longer exist at any effective datetime from the asAt datetime of deletion.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://local-unit-test-server.lusid.com:47048
configuration.host = "http://local-unit-test-server.lusid.com:47048"
# Create an instance of the API class
api_instance = lusid.LegalEntitiesApi(lusid.ApiClient(configuration))
id_type_scope = 'id_type_scope_example' # str | The scope of the legal entity identifier type.
id_type_code = 'id_type_code_example' # str | The code of the legal entity identifier type.
code = 'code_example' # str | Code of the legal entity under specified identifier type's scope and code. This together with defined              identifier type uniquely identifies the legal entity to delete.

try:
    # [EARLY ACCESS] Delete Legal Entity
    api_response = api_instance.delete_legal_entity(id_type_scope, id_type_code, code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LegalEntitiesApi->delete_legal_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_type_scope** | **str**| The scope of the legal entity identifier type. | 
 **id_type_code** | **str**| The code of the legal entity identifier type. | 
 **code** | **str**| Code of the legal entity under specified identifier type&#39;s scope and code. This together with defined              identifier type uniquely identifies the legal entity to delete. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response from deleting legal entity. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_legal_entity**
> LegalEntity get_legal_entity(id_type_scope, id_type_code, code, property_keys=property_keys, effective_at=effective_at, as_at=as_at)

[EARLY ACCESS] Get Legal Entity

Retrieve the definition of a legal entity.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://local-unit-test-server.lusid.com:47048
configuration.host = "http://local-unit-test-server.lusid.com:47048"
# Create an instance of the API class
api_instance = lusid.LegalEntitiesApi(lusid.ApiClient(configuration))
id_type_scope = 'id_type_scope_example' # str | Scope of the legal entity identifier type.
id_type_code = 'id_type_code_example' # str | Code of the legal entity identifier type.
code = 'code_example' # str | Code of the legal entity under specified identifier type's scope and code. This together with stated identifier type uniquely              identifies the legal entity.
property_keys = ['property_keys_example'] # list[str] | A list of property keys or identifier types (as property keys) from the \"LegalEntity\" domain to include for found legal entity.              These take the format {domain}/{scope}/{code} e.g. \"LegalEntity/ContactDetails/Address\". (optional)
effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the legal entity. Defaults to the current LUSID system datetime if not specified. (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the legal entity. Defaults to return the latest version of the legal entity if not specified. (optional)

try:
    # [EARLY ACCESS] Get Legal Entity
    api_response = api_instance.get_legal_entity(id_type_scope, id_type_code, code, property_keys=property_keys, effective_at=effective_at, as_at=as_at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LegalEntitiesApi->get_legal_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_type_scope** | **str**| Scope of the legal entity identifier type. | 
 **id_type_code** | **str**| Code of the legal entity identifier type. | 
 **code** | **str**| Code of the legal entity under specified identifier type&#39;s scope and code. This together with stated identifier type uniquely              identifies the legal entity. | 
 **property_keys** | [**list[str]**](str.md)| A list of property keys or identifier types (as property keys) from the \&quot;LegalEntity\&quot; domain to include for found legal entity.              These take the format {domain}/{scope}/{code} e.g. \&quot;LegalEntity/ContactDetails/Address\&quot;. | [optional] 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the legal entity. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the legal entity. Defaults to return the latest version of the legal entity if not specified. | [optional] 

### Return type

[**LegalEntity**](LegalEntity.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested legal entity |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_legal_entities**
> PagedResourceListOfLegalEntity list_legal_entities(id_type_scope, id_type_code, effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, property_keys=property_keys)

[EARLY ACCESS] List Legal Entities

List legal entities which has identifier of specific identifier type's scope and code, and satisfies filter criteria.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://local-unit-test-server.lusid.com:47048
configuration.host = "http://local-unit-test-server.lusid.com:47048"
# Create an instance of the API class
api_instance = lusid.LegalEntitiesApi(lusid.ApiClient(configuration))
id_type_scope = 'id_type_scope_example' # str | Scope of the legal entity identifier type.
id_type_code = 'id_type_code_example' # str | Code of the legal entity identifier type.
effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to list the people. Defaults to the current LUSID              system datetime if not specified. (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the people. Defaults to return the latest version              of each people if not specified. (optional)
page = 'page_example' # str | The pagination token to use to continue listing legal entities from a previous call to list legal entities. This  value is returned from the previous call. If a pagination token is provided the filter, effectiveAt  and asAt fields must not have changed since the original request. (optional)
limit = 56 # int | When paginating, limit the number of returned results to this many. Defaults to 65,535 if not specified. (optional)
filter = 'filter_example' # str | Expression to filter the result set.               Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)
property_keys = ['property_keys_example'] # list[str] | A list of property keys or identifier types (as property keys) from the \"LegalEntity\" domain to include for each legal entity.              These take the format {domain}/{scope}/{code} e.g. \"LegalEntity/ContactDetails/Address\". (optional)

try:
    # [EARLY ACCESS] List Legal Entities
    api_response = api_instance.list_legal_entities(id_type_scope, id_type_code, effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, property_keys=property_keys)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LegalEntitiesApi->list_legal_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_type_scope** | **str**| Scope of the legal entity identifier type. | 
 **id_type_code** | **str**| Code of the legal entity identifier type. | 
 **effective_at** | **str**| The effective datetime or cut label at which to list the people. Defaults to the current LUSID              system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the people. Defaults to return the latest version              of each people if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing legal entities from a previous call to list legal entities. This  value is returned from the previous call. If a pagination token is provided the filter, effectiveAt  and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 65,535 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set.               Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **property_keys** | [**list[str]**](str.md)| A list of property keys or identifier types (as property keys) from the \&quot;LegalEntity\&quot; domain to include for each legal entity.              These take the format {domain}/{scope}/{code} e.g. \&quot;LegalEntity/ContactDetails/Address\&quot;. | [optional] 

### Return type

[**PagedResourceListOfLegalEntity**](PagedResourceListOfLegalEntity.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Legal Entities with specified identifier type |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_legal_entity**
> LegalEntity upsert_legal_entity(upsert_legal_entity_request)

[EARLY ACCESS] Upsert Legal Entity

Create or update a legal entity

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://local-unit-test-server.lusid.com:47048
configuration.host = "http://local-unit-test-server.lusid.com:47048"
# Create an instance of the API class
api_instance = lusid.LegalEntitiesApi(lusid.ApiClient(configuration))
upsert_legal_entity_request = {"identifiers":{"legalEntity/ExternalIdentifier/LEI":{"key":"LegalEntity/ExternalIdentifier/LEI","value":{"labelValue":"LEI_12345678"}},"legalEntity/InternalIdentifier/InternalLeiId":{"key":"LegalEntity/InternalIdentifier/InternalLeiId","value":{"labelValue":"Internal_XHSP2038"}}},"properties":{"legalEntity/Details/Name":{"key":"LegalEntity/Details/Name","value":{"labelValue":"Legal Entity Inc."}},"legalEntity/Details/Country":{"key":"LegalEntity/Details/Country","value":{"labelValue":"United Kingdom"},"effectiveFrom":"2016-01-01T00:00:00.0000000+00:00"},"legalEntity/Status/Active":{"key":"LegalEntity/Status/Active","value":{"labelValue":"Active"},"effectiveFrom":"2016-07-01T00:00:00.0000000+00:00"}},"displayName":"LegalEntity1DisplayName","description":"LegalEntity1Description"} # UpsertLegalEntityRequest | Request to create or update a legal entity.

try:
    # [EARLY ACCESS] Upsert Legal Entity
    api_response = api_instance.upsert_legal_entity(upsert_legal_entity_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LegalEntitiesApi->upsert_legal_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_legal_entity_request** | [**UpsertLegalEntityRequest**](UpsertLegalEntityRequest.md)| Request to create or update a legal entity. | 

### Return type

[**LegalEntity**](LegalEntity.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created or updated legal entity |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

