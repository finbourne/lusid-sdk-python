# lusid.PersonsApi

All URIs are relative to *http://local-unit-test-server.lusid.com:41173*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_person_relations**](PersonsApi.md#get_person_relations) | **GET** /api/persons/{idTypeScope}/{idTypeCode}/{code}/relations | [DEPRECATED] Get Relations for Person


# **get_person_relations**
> ResourceListOfRelation get_person_relations(id_type_scope, id_type_code, code, effective_at=effective_at, as_at=as_at, filter=filter, identifier_types=identifier_types)

[DEPRECATED] Get Relations for Person

Get relations for the specified person.

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

# Defining host is optional and default to http://local-unit-test-server.lusid.com:41173
configuration.host = "http://local-unit-test-server.lusid.com:41173"
# Create an instance of the API class
api_instance = lusid.PersonsApi(lusid.ApiClient(configuration))
id_type_scope = 'id_type_scope_example' # str | Scope of the person identifier type.
id_type_code = 'id_type_code_example' # str | Code of the person identifier type.
code = 'code_example' # str | Code of the person under specified identifier type's scope and code. This together with stated identifier type uniquely              identifies the person.
effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to get relations. Defaults to the current LUSID system datetime if not specified. (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the person's relations. Defaults to return the latest LUSID AsAt time if not specified. (optional)
filter = 'filter_example' # str | Expression to filter the relations. Users should provide null or empty string for this field until further notice. (optional)
identifier_types = ['identifier_types_example'] # list[str] | Identifiers types (as property keys) used for referencing Persons or Legal Entities. These take the format              {domain}/{scope}/{code} e.g. \"Person/CompanyDetails/Role\". They must be from the \"Person\" or \"LegalEntity\" domain.              Only identifier types stated will be used to look up relevant entities in relations. If not applicable, provide an empty array. (optional)

try:
    # [DEPRECATED] Get Relations for Person
    api_response = api_instance.get_person_relations(id_type_scope, id_type_code, code, effective_at=effective_at, as_at=as_at, filter=filter, identifier_types=identifier_types)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonsApi->get_person_relations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_type_scope** | **str**| Scope of the person identifier type. | 
 **id_type_code** | **str**| Code of the person identifier type. | 
 **code** | **str**| Code of the person under specified identifier type&#39;s scope and code. This together with stated identifier type uniquely              identifies the person. | 
 **effective_at** | **str**| The effective datetime or cut label at which to get relations. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the person&#39;s relations. Defaults to return the latest LUSID AsAt time if not specified. | [optional] 
 **filter** | **str**| Expression to filter the relations. Users should provide null or empty string for this field until further notice. | [optional] 
 **identifier_types** | [**list[str]**](str.md)| Identifiers types (as property keys) used for referencing Persons or Legal Entities. These take the format              {domain}/{scope}/{code} e.g. \&quot;Person/CompanyDetails/Role\&quot;. They must be from the \&quot;Person\&quot; or \&quot;LegalEntity\&quot; domain.              Only identifier types stated will be used to look up relevant entities in relations. If not applicable, provide an empty array. | [optional] 

### Return type

[**ResourceListOfRelation**](ResourceListOfRelation.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The relations for the specified person. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

