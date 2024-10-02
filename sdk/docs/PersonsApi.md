# lusid.PersonsApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_person**](PersonsApi.md#delete_person) | **DELETE** /api/persons/{idTypeScope}/{idTypeCode}/{code} | DeletePerson: Delete person
[**delete_person_access_metadata**](PersonsApi.md#delete_person_access_metadata) | **DELETE** /api/persons/{idTypeScope}/{idTypeCode}/{code}/metadata/{metadataKey} | [EARLY ACCESS] DeletePersonAccessMetadata: Delete a Person Access Metadata entry
[**delete_person_identifiers**](PersonsApi.md#delete_person_identifiers) | **DELETE** /api/persons/{idTypeScope}/{idTypeCode}/{code}/identifiers | [EARLY ACCESS] DeletePersonIdentifiers: Delete Person Identifiers
[**delete_person_properties**](PersonsApi.md#delete_person_properties) | **DELETE** /api/persons/{idTypeScope}/{idTypeCode}/{code}/properties | [EARLY ACCESS] DeletePersonProperties: Delete Person Properties
[**get_all_person_access_metadata**](PersonsApi.md#get_all_person_access_metadata) | **GET** /api/persons/{idTypeScope}/{idTypeCode}/{code}/metadata | [EARLY ACCESS] GetAllPersonAccessMetadata: Get Access Metadata rules for a Person
[**get_person**](PersonsApi.md#get_person) | **GET** /api/persons/{idTypeScope}/{idTypeCode}/{code} | [EARLY ACCESS] GetPerson: Get Person
[**get_person_access_metadata_by_key**](PersonsApi.md#get_person_access_metadata_by_key) | **GET** /api/persons/{idTypeScope}/{idTypeCode}/{code}/metadata/{metadataKey} | [EARLY ACCESS] GetPersonAccessMetadataByKey: Get an entry identified by a metadataKey in the Access Metadata of a Person
[**get_person_property_time_series**](PersonsApi.md#get_person_property_time_series) | **GET** /api/persons/{idTypeScope}/{idTypeCode}/{code}/properties/time-series | [EARLY ACCESS] GetPersonPropertyTimeSeries: Get Person Property Time Series
[**get_person_relations**](PersonsApi.md#get_person_relations) | **GET** /api/persons/{idTypeScope}/{idTypeCode}/{code}/relations | [EARLY ACCESS] GetPersonRelations: Get Relations for Person
[**get_person_relationships**](PersonsApi.md#get_person_relationships) | **GET** /api/persons/{idTypeScope}/{idTypeCode}/{code}/relationships | [EARLY ACCESS] GetPersonRelationships: Get Relationships for Person
[**list_all_persons**](PersonsApi.md#list_all_persons) | **GET** /api/persons | [EARLY ACCESS] ListAllPersons: List All Persons
[**list_persons**](PersonsApi.md#list_persons) | **GET** /api/persons/{idTypeScope}/{idTypeCode} | [EARLY ACCESS] ListPersons: List Persons
[**patch_person_access_metadata**](PersonsApi.md#patch_person_access_metadata) | **PATCH** /api/persons/{idTypeScope}/{idTypeCode}/{code}/metadata | [EARLY ACCESS] PatchPersonAccessMetadata: Patch Access Metadata rules for a Person.
[**set_person_identifiers**](PersonsApi.md#set_person_identifiers) | **POST** /api/persons/{idTypeScope}/{idTypeCode}/{code}/identifiers | [EARLY ACCESS] SetPersonIdentifiers: Set Person Identifiers
[**set_person_properties**](PersonsApi.md#set_person_properties) | **POST** /api/persons/{idTypeScope}/{idTypeCode}/{code}/properties | [EARLY ACCESS] SetPersonProperties: Set Person Properties
[**upsert_person**](PersonsApi.md#upsert_person) | **POST** /api/persons | UpsertPerson: Upsert Person
[**upsert_person_access_metadata**](PersonsApi.md#upsert_person_access_metadata) | **PUT** /api/persons/{idTypeScope}/{idTypeCode}/{code}/metadata/{metadataKey} | [EARLY ACCESS] UpsertPersonAccessMetadata: Upsert a Person Access Metadata entry associated with a specific metadataKey. This creates or updates the data in LUSID.
[**upsert_persons**](PersonsApi.md#upsert_persons) | **POST** /api/persons/$batchUpsert | [EARLY ACCESS] UpsertPersons: Pluralised Upsert of Persons


# **delete_person**
> DeletedEntityResponse delete_person(id_type_scope, id_type_code, code)

DeletePerson: Delete person

Delete a person. Deletion will be valid from the person's creation datetime.  This means that the person will no longer exist at any effective datetime from the asAt datetime of deletion.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    PersonsApi
)

async def main():

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

    # Use the lusid ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(PersonsApi)
        id_type_scope = 'id_type_scope_example' # str | The scope of the person identifier type.
        id_type_code = 'id_type_code_example' # str | The code of the person identifier type.
        code = 'code_example' # str | Code of the person under specified identifier type scope and code. This together with defined              identifier type uniquely identifies the person to delete.

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.delete_person(id_type_scope, id_type_code, code, opts=opts)

            # DeletePerson: Delete person
            api_response = await api_instance.delete_person(id_type_scope, id_type_code, code)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling PersonsApi->delete_person: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_type_scope** | **str**| The scope of the person identifier type. | 
 **id_type_code** | **str**| The code of the person identifier type. | 
 **code** | **str**| Code of the person under specified identifier type scope and code. This together with defined              identifier type uniquely identifies the person to delete. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response from deleting person. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_person_access_metadata**
> DeletedEntityResponse delete_person_access_metadata(id_type_scope, id_type_code, code, metadata_key, effective_at=effective_at, effective_until=effective_until)

[EARLY ACCESS] DeletePersonAccessMetadata: Delete a Person Access Metadata entry

Deletes the Person Access Metadata entry that exactly matches the provided identifier parts.    It is important to always check to verify success (or failure).

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    PersonsApi
)

async def main():

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

    # Use the lusid ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(PersonsApi)
        id_type_scope = 'id_type_scope_example' # str | Scope of the person identifier.
        id_type_code = 'id_type_code_example' # str | Code of the person identifier.
        code = 'code_example' # str | Code of the person under specified identifier type's scope and code.
        metadata_key = 'metadata_key_example' # str | Key of the metadata entry to retrieve
        effective_at = 'effective_at_example' # str | The effective date to delete at, if this is not supplied, it will delete all data found (optional)
        effective_until = '2013-10-20T19:20:30+01:00' # datetime | The effective date until which the delete is valid. If not supplied this will be valid indefinitely, or until the next 'effectiveAt' date of the Access Metadata (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.delete_person_access_metadata(id_type_scope, id_type_code, code, metadata_key, effective_at=effective_at, effective_until=effective_until, opts=opts)

            # [EARLY ACCESS] DeletePersonAccessMetadata: Delete a Person Access Metadata entry
            api_response = await api_instance.delete_person_access_metadata(id_type_scope, id_type_code, code, metadata_key, effective_at=effective_at, effective_until=effective_until)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling PersonsApi->delete_person_access_metadata: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_type_scope** | **str**| Scope of the person identifier. | 
 **id_type_code** | **str**| Code of the person identifier. | 
 **code** | **str**| Code of the person under specified identifier type&#39;s scope and code. | 
 **metadata_key** | **str**| Key of the metadata entry to retrieve | 
 **effective_at** | **str**| The effective date to delete at, if this is not supplied, it will delete all data found | [optional] 
 **effective_until** | **datetime**| The effective date until which the delete is valid. If not supplied this will be valid indefinitely, or until the next &#39;effectiveAt&#39; date of the Access Metadata | [optional] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Access Metadata with the given metadataKey has been deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_person_identifiers**
> DeletedEntityResponse delete_person_identifiers(id_type_scope, id_type_code, code, property_keys, effective_at=effective_at)

[EARLY ACCESS] DeletePersonIdentifiers: Delete Person Identifiers

Delete identifiers that belong to the given property keys of the person.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    PersonsApi
)

async def main():

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

    # Use the lusid ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(PersonsApi)
        id_type_scope = 'id_type_scope_example' # str | Scope of the person identifier type.
        id_type_code = 'id_type_code_example' # str | Code of the person identifier type.
        code = 'code_example' # str | Code of the person under specified identifier type's scope and code. This together with stated identifier type uniquely              identifies the person.
        property_keys = ['property_keys_example'] # List[str] | The property keys of the identifiers to delete. These take the format              {domain}/{scope}/{code} e.g. \"Person/CompanyDetails/Role\". Each property must be from the \"Person\" domain. Identifiers or identifiers not specified in request will not be changed.
        effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to delete the identifiers. Defaults to the current LUSID system datetime if not specified.              Must not include an effective datetime if identifiers are perpetual. (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.delete_person_identifiers(id_type_scope, id_type_code, code, property_keys, effective_at=effective_at, opts=opts)

            # [EARLY ACCESS] DeletePersonIdentifiers: Delete Person Identifiers
            api_response = await api_instance.delete_person_identifiers(id_type_scope, id_type_code, code, property_keys, effective_at=effective_at)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling PersonsApi->delete_person_identifiers: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_type_scope** | **str**| Scope of the person identifier type. | 
 **id_type_code** | **str**| Code of the person identifier type. | 
 **code** | **str**| Code of the person under specified identifier type&#39;s scope and code. This together with stated identifier type uniquely              identifies the person. | 
 **property_keys** | [**List[str]**](str.md)| The property keys of the identifiers to delete. These take the format              {domain}/{scope}/{code} e.g. \&quot;Person/CompanyDetails/Role\&quot;. Each property must be from the \&quot;Person\&quot; domain. Identifiers or identifiers not specified in request will not be changed. | 
 **effective_at** | **str**| The effective datetime or cut label at which to delete the identifiers. Defaults to the current LUSID system datetime if not specified.              Must not include an effective datetime if identifiers are perpetual. | [optional] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the identifiers were deleted from the specified person |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_person_properties**
> DeletedEntityResponse delete_person_properties(id_type_scope, id_type_code, code, property_keys, effective_at=effective_at)

[EARLY ACCESS] DeletePersonProperties: Delete Person Properties

Delete all properties that belong to the given property keys of the person.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    PersonsApi
)

async def main():

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

    # Use the lusid ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(PersonsApi)
        id_type_scope = 'id_type_scope_example' # str | Scope of the person identifier type.
        id_type_code = 'id_type_code_example' # str | Code of the person identifier type.
        code = 'code_example' # str | Code of the person under specified identifier type's scope and code. This together with stated identifier type uniquely              identifies the person.
        property_keys = ['property_keys_example'] # List[str] | The property keys of the person's properties to delete. These take the format              {domain}/{scope}/{code} e.g. \"Person/CompanyDetails/Role\". Each property must be from the \"Person\" domain. Properties or identifiers not specified in request will not be changed.
        effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to delete time-variant properties from.              The property must exist at the specified 'effectiveAt' datetime. If the 'effectiveAt' is not provided or is              before the time-variant property exists then a failure is returned. Do not specify this parameter if any of              the properties to delete are perpetual. (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.delete_person_properties(id_type_scope, id_type_code, code, property_keys, effective_at=effective_at, opts=opts)

            # [EARLY ACCESS] DeletePersonProperties: Delete Person Properties
            api_response = await api_instance.delete_person_properties(id_type_scope, id_type_code, code, property_keys, effective_at=effective_at)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling PersonsApi->delete_person_properties: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_type_scope** | **str**| Scope of the person identifier type. | 
 **id_type_code** | **str**| Code of the person identifier type. | 
 **code** | **str**| Code of the person under specified identifier type&#39;s scope and code. This together with stated identifier type uniquely              identifies the person. | 
 **property_keys** | [**List[str]**](str.md)| The property keys of the person&#39;s properties to delete. These take the format              {domain}/{scope}/{code} e.g. \&quot;Person/CompanyDetails/Role\&quot;. Each property must be from the \&quot;Person\&quot; domain. Properties or identifiers not specified in request will not be changed. | 
 **effective_at** | **str**| The effective datetime or cut label at which to delete time-variant properties from.              The property must exist at the specified &#39;effectiveAt&#39; datetime. If the &#39;effectiveAt&#39; is not provided or is              before the time-variant property exists then a failure is returned. Do not specify this parameter if any of              the properties to delete are perpetual. | [optional] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the properties were deleted from the specified person |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_all_person_access_metadata**
> Dict[str, List[AccessMetadataValue]] get_all_person_access_metadata(id_type_scope, id_type_code, code, effective_at=effective_at, as_at=as_at)

[EARLY ACCESS] GetAllPersonAccessMetadata: Get Access Metadata rules for a Person

Pass the Scope and Code of the Person identifier along with the person code parameter to retrieve the associated Access Metadata

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    PersonsApi
)

async def main():

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

    # Use the lusid ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(PersonsApi)
        id_type_scope = 'id_type_scope_example' # str | Scope of the person identifier.
        id_type_code = 'id_type_code_example' # str | Code of the person identifier.
        code = 'code_example' # str | Code of the person under specified identifier type's scope and code.
        effective_at = 'effective_at_example' # str | The effectiveAt datetime at which to retrieve the Access Metadata (optional)
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Access Metadata (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.get_all_person_access_metadata(id_type_scope, id_type_code, code, effective_at=effective_at, as_at=as_at, opts=opts)

            # [EARLY ACCESS] GetAllPersonAccessMetadata: Get Access Metadata rules for a Person
            api_response = await api_instance.get_all_person_access_metadata(id_type_scope, id_type_code, code, effective_at=effective_at, as_at=as_at)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling PersonsApi->get_all_person_access_metadata: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_type_scope** | **str**| Scope of the person identifier. | 
 **id_type_code** | **str**| Code of the person identifier. | 
 **code** | **str**| Code of the person under specified identifier type&#39;s scope and code. | 
 **effective_at** | **str**| The effectiveAt datetime at which to retrieve the Access Metadata | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Access Metadata | [optional] 

### Return type

**Dict[str, List[AccessMetadataValue]]**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The access metadata for the Person or any failure. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_person**
> Person get_person(id_type_scope, id_type_code, code, property_keys=property_keys, effective_at=effective_at, as_at=as_at, relationship_definition_ids=relationship_definition_ids)

[EARLY ACCESS] GetPerson: Get Person

Retrieve the definition of a person.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    PersonsApi
)

async def main():

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

    # Use the lusid ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(PersonsApi)
        id_type_scope = 'id_type_scope_example' # str | Scope of the person identifier type.
        id_type_code = 'id_type_code_example' # str | Code of the person identifier type.
        code = 'code_example' # str | Code of the person under specified scope and code. This together with stated identifier type uniquely              identifies the person.
        property_keys = ['property_keys_example'] # List[str] | A list of property keys from the \"Person\" domain to decorate onto the person,               or from any domain that supports relationships to decorate onto related entities.              These take the format {domain}/{scope}/{code} e.g. \"Person/ContactDetails/Address\". (optional)
        effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the person. Defaults to the current LUSID system datetime if not specified. (optional)
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the person. Defaults to return the latest version of the person if not specified. (optional)
        relationship_definition_ids = ['relationship_definition_ids_example'] # List[str] | A list of relationship definitions that are used to decorate related entities              onto the person in the response. These must take the form {relationshipDefinitionScope}/{relationshipDefinitionCode}. (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.get_person(id_type_scope, id_type_code, code, property_keys=property_keys, effective_at=effective_at, as_at=as_at, relationship_definition_ids=relationship_definition_ids, opts=opts)

            # [EARLY ACCESS] GetPerson: Get Person
            api_response = await api_instance.get_person(id_type_scope, id_type_code, code, property_keys=property_keys, effective_at=effective_at, as_at=as_at, relationship_definition_ids=relationship_definition_ids)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling PersonsApi->get_person: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_type_scope** | **str**| Scope of the person identifier type. | 
 **id_type_code** | **str**| Code of the person identifier type. | 
 **code** | **str**| Code of the person under specified scope and code. This together with stated identifier type uniquely              identifies the person. | 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the \&quot;Person\&quot; domain to decorate onto the person,               or from any domain that supports relationships to decorate onto related entities.              These take the format {domain}/{scope}/{code} e.g. \&quot;Person/ContactDetails/Address\&quot;. | [optional] 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the person. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the person. Defaults to return the latest version of the person if not specified. | [optional] 
 **relationship_definition_ids** | [**List[str]**](str.md)| A list of relationship definitions that are used to decorate related entities              onto the person in the response. These must take the form {relationshipDefinitionScope}/{relationshipDefinitionCode}. | [optional] 

### Return type

[**Person**](Person.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested person definition |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_person_access_metadata_by_key**
> List[AccessMetadataValue] get_person_access_metadata_by_key(id_type_scope, id_type_code, code, metadata_key, effective_at=effective_at, as_at=as_at)

[EARLY ACCESS] GetPersonAccessMetadataByKey: Get an entry identified by a metadataKey in the Access Metadata of a Person

Get a specific Person Access Metadata by specifying the corresponding identifier parts and Person code                No matching will be performed through this endpoint. To retrieve an entry, it is necessary to specify, exactly, the identifier of the entry

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    PersonsApi
)

async def main():

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

    # Use the lusid ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(PersonsApi)
        id_type_scope = 'id_type_scope_example' # str | Scope of the person identifier.
        id_type_code = 'id_type_code_example' # str | Code of the person identifier.
        code = 'code_example' # str | Code of the person under specified identifier type's scope and code.
        metadata_key = 'metadata_key_example' # str | Key of the metadata entry to retrieve
        effective_at = 'effective_at_example' # str | The effectiveAt datetime at which to retrieve the Access Metadata (optional)
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Access Metadata (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.get_person_access_metadata_by_key(id_type_scope, id_type_code, code, metadata_key, effective_at=effective_at, as_at=as_at, opts=opts)

            # [EARLY ACCESS] GetPersonAccessMetadataByKey: Get an entry identified by a metadataKey in the Access Metadata of a Person
            api_response = await api_instance.get_person_access_metadata_by_key(id_type_scope, id_type_code, code, metadata_key, effective_at=effective_at, as_at=as_at)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling PersonsApi->get_person_access_metadata_by_key: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_type_scope** | **str**| Scope of the person identifier. | 
 **id_type_code** | **str**| Code of the person identifier. | 
 **code** | **str**| Code of the person under specified identifier type&#39;s scope and code. | 
 **metadata_key** | **str**| Key of the metadata entry to retrieve | 
 **effective_at** | **str**| The effectiveAt datetime at which to retrieve the Access Metadata | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Access Metadata | [optional] 

### Return type

[**List[AccessMetadataValue]**](AccessMetadataValue.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully retrieved Person access metadata filtered by metadataKey or any failure. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_person_property_time_series**
> ResourceListOfPropertyInterval get_person_property_time_series(id_type_scope, id_type_code, code, property_key, as_at=as_at, filter=filter, page=page, limit=limit)

[EARLY ACCESS] GetPersonPropertyTimeSeries: Get Person Property Time Series

List the complete time series of a person property.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    PersonsApi
)

async def main():

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

    # Use the lusid ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(PersonsApi)
        id_type_scope = 'id_type_scope_example' # str | Scope of the person identifier type.
        id_type_code = 'id_type_code_example' # str | Code of the person identifier type.
        code = 'code_example' # str | Code of the person under specified identifier type's scope and code. This together with stated identifier type uniquely identifies the person.
        property_key = 'property_key_example' # str | The property key of the property that will have its history shown. These must be in the format {domain}/{scope}/{code} e.g. \"Person/CompanyDetails/Role\".              Each property must be from the \"Person\" domain.
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the person's property history. Defaults to return the current datetime if not supplied. (optional)
        filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)
        page = 'page_example' # str | The pagination token to use to continue listing properties from a previous call to get property time series.              This value is returned from the previous call. If a pagination token is provided the filter and asAt fields              must not have changed since the original request. (optional)
        limit = 56 # int | When paginating, limit the number of returned results to this many. (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.get_person_property_time_series(id_type_scope, id_type_code, code, property_key, as_at=as_at, filter=filter, page=page, limit=limit, opts=opts)

            # [EARLY ACCESS] GetPersonPropertyTimeSeries: Get Person Property Time Series
            api_response = await api_instance.get_person_property_time_series(id_type_scope, id_type_code, code, property_key, as_at=as_at, filter=filter, page=page, limit=limit)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling PersonsApi->get_person_property_time_series: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_type_scope** | **str**| Scope of the person identifier type. | 
 **id_type_code** | **str**| Code of the person identifier type. | 
 **code** | **str**| Code of the person under specified identifier type&#39;s scope and code. This together with stated identifier type uniquely identifies the person. | 
 **property_key** | **str**| The property key of the property that will have its history shown. These must be in the format {domain}/{scope}/{code} e.g. \&quot;Person/CompanyDetails/Role\&quot;.              Each property must be from the \&quot;Person\&quot; domain. | 
 **as_at** | **datetime**| The asAt datetime at which to list the person&#39;s property history. Defaults to return the current datetime if not supplied. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **page** | **str**| The pagination token to use to continue listing properties from a previous call to get property time series.              This value is returned from the previous call. If a pagination token is provided the filter and asAt fields              must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 

### Return type

[**ResourceListOfPropertyInterval**](ResourceListOfPropertyInterval.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The time series of the property |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_person_relations**
> ResourceListOfRelation get_person_relations(id_type_scope, id_type_code, code, effective_at=effective_at, as_at=as_at, filter=filter, identifier_types=identifier_types)

[EARLY ACCESS] GetPersonRelations: Get Relations for Person

Get relations for the specified person.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    PersonsApi
)

async def main():

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

    # Use the lusid ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(PersonsApi)
        id_type_scope = 'id_type_scope_example' # str | Scope of the person identifier type.
        id_type_code = 'id_type_code_example' # str | Code of the person identifier type.
        code = 'code_example' # str | Code of the person under specified identifier type's scope and code. This together with stated identifier type uniquely              identifies the person.
        effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to get relations. Defaults to the current LUSID system datetime if not specified. (optional)
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the person's relations. Defaults to return the latest LUSID AsAt time if not specified. (optional)
        filter = 'filter_example' # str | Expression to filter the relations. Users should provide null or empty string for this field until further notice. (optional)
        identifier_types = ['identifier_types_example'] # List[str] | Identifiers types (as property keys) used for referencing Persons or Legal Entities. These take the format              {domain}/{scope}/{code} e.g. \"Person/CompanyDetails/Role\". They must be from the \"Person\" or \"LegalEntity\" domain.              Only identifier types stated will be used to look up relevant entities in relations. If not applicable, provide an empty array. (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.get_person_relations(id_type_scope, id_type_code, code, effective_at=effective_at, as_at=as_at, filter=filter, identifier_types=identifier_types, opts=opts)

            # [EARLY ACCESS] GetPersonRelations: Get Relations for Person
            api_response = await api_instance.get_person_relations(id_type_scope, id_type_code, code, effective_at=effective_at, as_at=as_at, filter=filter, identifier_types=identifier_types)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling PersonsApi->get_person_relations: %s\n" % e)

asyncio.run(main())
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
 **identifier_types** | [**List[str]**](str.md)| Identifiers types (as property keys) used for referencing Persons or Legal Entities. These take the format              {domain}/{scope}/{code} e.g. \&quot;Person/CompanyDetails/Role\&quot;. They must be from the \&quot;Person\&quot; or \&quot;LegalEntity\&quot; domain.              Only identifier types stated will be used to look up relevant entities in relations. If not applicable, provide an empty array. | [optional] 

### Return type

[**ResourceListOfRelation**](ResourceListOfRelation.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The relations for the specified person. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_person_relationships**
> ResourceListOfRelationship get_person_relationships(id_type_scope, id_type_code, code, effective_at=effective_at, as_at=as_at, filter=filter, identifier_types=identifier_types)

[EARLY ACCESS] GetPersonRelationships: Get Relationships for Person

Get relationships for the specified person.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    PersonsApi
)

async def main():

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

    # Use the lusid ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(PersonsApi)
        id_type_scope = 'id_type_scope_example' # str | Scope of the person's identifier type.
        id_type_code = 'id_type_code_example' # str | Code of the person's identifier type.
        code = 'code_example' # str | Code of the person under specified identifier type's scope and code. This together with stated identifier type uniquely              identifies the person.
        effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to get relationships. Defaults to the current LUSID system datetime if not specified. (optional)
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve relationships. Defaults to return the latest LUSID AsAt time if not specified. (optional)
        filter = 'filter_example' # str | Expression to filter relationships. Users should provide null or empty string for this field until further notice. (optional)
        identifier_types = ['identifier_types_example'] # List[str] | Identifier types (as property keys) used for referencing Persons or Legal Entities.              These can be specified from the 'Person' or 'LegalEntity' domains and have the format {domain}/{scope}/{code}, for example              'Person/CompanyDetails/Role'. An Empty array may be used to return all related Entities. (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.get_person_relationships(id_type_scope, id_type_code, code, effective_at=effective_at, as_at=as_at, filter=filter, identifier_types=identifier_types, opts=opts)

            # [EARLY ACCESS] GetPersonRelationships: Get Relationships for Person
            api_response = await api_instance.get_person_relationships(id_type_scope, id_type_code, code, effective_at=effective_at, as_at=as_at, filter=filter, identifier_types=identifier_types)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling PersonsApi->get_person_relationships: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_type_scope** | **str**| Scope of the person&#39;s identifier type. | 
 **id_type_code** | **str**| Code of the person&#39;s identifier type. | 
 **code** | **str**| Code of the person under specified identifier type&#39;s scope and code. This together with stated identifier type uniquely              identifies the person. | 
 **effective_at** | **str**| The effective datetime or cut label at which to get relationships. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve relationships. Defaults to return the latest LUSID AsAt time if not specified. | [optional] 
 **filter** | **str**| Expression to filter relationships. Users should provide null or empty string for this field until further notice. | [optional] 
 **identifier_types** | [**List[str]**](str.md)| Identifier types (as property keys) used for referencing Persons or Legal Entities.              These can be specified from the &#39;Person&#39; or &#39;LegalEntity&#39; domains and have the format {domain}/{scope}/{code}, for example              &#39;Person/CompanyDetails/Role&#39;. An Empty array may be used to return all related Entities. | [optional] 

### Return type

[**ResourceListOfRelationship**](ResourceListOfRelationship.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The relationships for the specified person. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_all_persons**
> ResourceListOfPerson list_all_persons(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, property_keys=property_keys, relationship_definition_ids=relationship_definition_ids)

[EARLY ACCESS] ListAllPersons: List All Persons

List all persons which the user is entitled to see.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    PersonsApi
)

async def main():

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

    # Use the lusid ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(PersonsApi)
        effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to list the people. Defaults to the current LUSID              system datetime if not specified. (optional)
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the people. Defaults to return the latest version              of each people if not specified. (optional)
        page = 'page_example' # str | The pagination token to use to continue listing persons from a previous call to list persons. This              value is returned from the previous call. If a pagination token is provided the filter, effectiveAt              and asAt fields must not have changed since the original request. (optional)
        limit = 56 # int | When paginating, limit the number of returned results to this many. Defaults to 5000 if not specified. (optional)
        filter = 'filter_example' # str | Expression to filter the result set.               For example, to filter on the display name, use \"displayName eq 'John'\"              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)
        property_keys = ['property_keys_example'] # List[str] | A list of property keys from the \"Person\" domain to decorate onto each person,               or from any domain that supports relationships to decorate onto related entities.              These take the format {domain}/{scope}/{code} e.g. \"Person/ContactDetails/Address\". (optional)
        relationship_definition_ids = ['relationship_definition_ids_example'] # List[str] | A list of relationship definitions that are used to decorate related entities              onto the persons in the response. These must take the form {relationshipDefinitionScope}/{relationshipDefinitionCode}. (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.list_all_persons(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, property_keys=property_keys, relationship_definition_ids=relationship_definition_ids, opts=opts)

            # [EARLY ACCESS] ListAllPersons: List All Persons
            api_response = await api_instance.list_all_persons(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, property_keys=property_keys, relationship_definition_ids=relationship_definition_ids)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling PersonsApi->list_all_persons: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **effective_at** | **str**| The effective datetime or cut label at which to list the people. Defaults to the current LUSID              system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the people. Defaults to return the latest version              of each people if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing persons from a previous call to list persons. This              value is returned from the previous call. If a pagination token is provided the filter, effectiveAt              and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 5000 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set.               For example, to filter on the display name, use \&quot;displayName eq &#39;John&#39;\&quot;              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the \&quot;Person\&quot; domain to decorate onto each person,               or from any domain that supports relationships to decorate onto related entities.              These take the format {domain}/{scope}/{code} e.g. \&quot;Person/ContactDetails/Address\&quot;. | [optional] 
 **relationship_definition_ids** | [**List[str]**](str.md)| A list of relationship definitions that are used to decorate related entities              onto the persons in the response. These must take the form {relationshipDefinitionScope}/{relationshipDefinitionCode}. | [optional] 

### Return type

[**ResourceListOfPerson**](ResourceListOfPerson.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Existing people |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_persons**
> PagedResourceListOfPerson list_persons(id_type_scope, id_type_code, effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, property_keys=property_keys, relationship_definition_ids=relationship_definition_ids)

[EARLY ACCESS] ListPersons: List Persons

List persons which have identifiers of a specific identifier type's scope and code, and satisfies filter criteria.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    PersonsApi
)

async def main():

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

    # Use the lusid ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(PersonsApi)
        id_type_scope = 'id_type_scope_example' # str | Scope of the person identifier type.
        id_type_code = 'id_type_code_example' # str | Code of the person identifier type.
        effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to list the people. Defaults to the current LUSID              system datetime if not specified. (optional)
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the people. Defaults to return the latest version              of each people if not specified. (optional)
        page = 'page_example' # str | The pagination token to use to continue listing persons from a previous call to list persons. This              value is returned from the previous call. If a pagination token is provided the filter, effectiveAt              and asAt fields must not have changed since the original request. (optional)
        limit = 56 # int | When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. (optional)
        filter = 'filter_example' # str | Expression to filter the result set.               For example, to filter on the LUPID, use \"lusidPersonId eq 'string'\"              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)
        property_keys = ['property_keys_example'] # List[str] | A list of property keys from the \"Person\" domain to decorate onto each person,               or from any domain that supports relationships to decorate onto related entities.              These take the format {domain}/{scope}/{code} e.g. \"Person/ContactDetails/Address\". (optional)
        relationship_definition_ids = ['relationship_definition_ids_example'] # List[str] | A list of relationship definitions that are used to decorate related entities              onto the persons in the response. These must take the form {relationshipDefinitionScope}/{relationshipDefinitionCode}. (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.list_persons(id_type_scope, id_type_code, effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, property_keys=property_keys, relationship_definition_ids=relationship_definition_ids, opts=opts)

            # [EARLY ACCESS] ListPersons: List Persons
            api_response = await api_instance.list_persons(id_type_scope, id_type_code, effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, property_keys=property_keys, relationship_definition_ids=relationship_definition_ids)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling PersonsApi->list_persons: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_type_scope** | **str**| Scope of the person identifier type. | 
 **id_type_code** | **str**| Code of the person identifier type. | 
 **effective_at** | **str**| The effective datetime or cut label at which to list the people. Defaults to the current LUSID              system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the people. Defaults to return the latest version              of each people if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing persons from a previous call to list persons. This              value is returned from the previous call. If a pagination token is provided the filter, effectiveAt              and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set.               For example, to filter on the LUPID, use \&quot;lusidPersonId eq &#39;string&#39;\&quot;              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the \&quot;Person\&quot; domain to decorate onto each person,               or from any domain that supports relationships to decorate onto related entities.              These take the format {domain}/{scope}/{code} e.g. \&quot;Person/ContactDetails/Address\&quot;. | [optional] 
 **relationship_definition_ids** | [**List[str]**](str.md)| A list of relationship definitions that are used to decorate related entities              onto the persons in the response. These must take the form {relationshipDefinitionScope}/{relationshipDefinitionCode}. | [optional] 

### Return type

[**PagedResourceListOfPerson**](PagedResourceListOfPerson.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | People in specified scope |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **patch_person_access_metadata**
> Dict[str, List[AccessMetadataValue]] patch_person_access_metadata(id_type_scope, id_type_code, code, access_metadata_operation, effective_at=effective_at, effective_until=effective_until)

[EARLY ACCESS] PatchPersonAccessMetadata: Patch Access Metadata rules for a Person.

Patch Person Access Metadata Rules in a single scope.  The behaviour is defined by the JSON Patch specification.                Currently only 'add' is a supported operation on the patch document.    Currently only valid metadata keys are supported paths on the patch document.                The response will return any affected Person Access Metadata rules or a failure message if unsuccessful.                It is important to always check to verify success (or failure).                Multiple rules for a metadataKey can exist with different effective at dates, when resources are accessed the rule that is active for the current time will be fetched.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    PersonsApi
)

async def main():

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

    # Use the lusid ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(PersonsApi)
        id_type_scope = 'id_type_scope_example' # str | Scope of the person identifier.
        id_type_code = 'id_type_code_example' # str | Code of the person identifier.
        code = 'code_example' # str | Code of the person under specified identifier type's scope and code.
        access_metadata_operation = [{"value":[{"value":"SilverLicence","provider":"TestDataProvider"}],"path":"/exampleMetadataKey","op":"add"}] # List[AccessMetadataOperation] | The Json Patch document
        effective_at = 'effective_at_example' # str | The effectiveAt datetime at which to upsert the Access Metadata (optional)
        effective_until = '2013-10-20T19:20:30+01:00' # datetime | The effective datetime until which the Access Metadata is valid. If not supplied this will be valid indefinitely, or until the next 'effectiveAt' datetime of the Access Metadata (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.patch_person_access_metadata(id_type_scope, id_type_code, code, access_metadata_operation, effective_at=effective_at, effective_until=effective_until, opts=opts)

            # [EARLY ACCESS] PatchPersonAccessMetadata: Patch Access Metadata rules for a Person.
            api_response = await api_instance.patch_person_access_metadata(id_type_scope, id_type_code, code, access_metadata_operation, effective_at=effective_at, effective_until=effective_until)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling PersonsApi->patch_person_access_metadata: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_type_scope** | **str**| Scope of the person identifier. | 
 **id_type_code** | **str**| Code of the person identifier. | 
 **code** | **str**| Code of the person under specified identifier type&#39;s scope and code. | 
 **access_metadata_operation** | [**List[AccessMetadataOperation]**](AccessMetadataOperation.md)| The Json Patch document | 
 **effective_at** | **str**| The effectiveAt datetime at which to upsert the Access Metadata | [optional] 
 **effective_until** | **datetime**| The effective datetime until which the Access Metadata is valid. If not supplied this will be valid indefinitely, or until the next &#39;effectiveAt&#39; datetime of the Access Metadata | [optional] 

### Return type

**Dict[str, List[AccessMetadataValue]]**

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully patched items. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **set_person_identifiers**
> Person set_person_identifiers(id_type_scope, id_type_code, code, set_person_identifiers_request)

[EARLY ACCESS] SetPersonIdentifiers: Set Person Identifiers

Set identifiers of the person.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    PersonsApi
)

async def main():

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

    # Use the lusid ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(PersonsApi)
        id_type_scope = 'id_type_scope_example' # str | Scope of the person identifier type.
        id_type_code = 'id_type_code_example' # str | Code of the person identifier type.
        code = 'code_example' # str | Code of the person under specified identifier type's scope and code. This together with stated identifier type uniquely              identifies the person.

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # set_person_identifiers_request = SetPersonIdentifiersRequest.from_json("")
        # set_person_identifiers_request = SetPersonIdentifiersRequest.from_dict({})
        set_person_identifiers_request = SetPersonIdentifiersRequest()

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.set_person_identifiers(id_type_scope, id_type_code, code, set_person_identifiers_request, opts=opts)

            # [EARLY ACCESS] SetPersonIdentifiers: Set Person Identifiers
            api_response = await api_instance.set_person_identifiers(id_type_scope, id_type_code, code, set_person_identifiers_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling PersonsApi->set_person_identifiers: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_type_scope** | **str**| Scope of the person identifier type. | 
 **id_type_code** | **str**| Code of the person identifier type. | 
 **code** | **str**| Code of the person under specified identifier type&#39;s scope and code. This together with stated identifier type uniquely              identifies the person. | 
 **set_person_identifiers_request** | [**SetPersonIdentifiersRequest**](SetPersonIdentifiersRequest.md)| Request containing identifiers to set for the person. Identifiers not specified in request will not be changed. | 

### Return type

[**Person**](Person.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Person with updated identifiers. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **set_person_properties**
> Person set_person_properties(id_type_scope, id_type_code, code, set_person_properties_request)

[EARLY ACCESS] SetPersonProperties: Set Person Properties

Set properties of the person.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    PersonsApi
)

async def main():

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

    # Use the lusid ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(PersonsApi)
        id_type_scope = 'id_type_scope_example' # str | Scope of the person identifier type.
        id_type_code = 'id_type_code_example' # str | Code of the person identifier type.
        code = 'code_example' # str | Code of the person under specified identifier type's scope and code. This together with stated identifier type uniquely              identifies the person.

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # set_person_properties_request = SetPersonPropertiesRequest.from_json("")
        # set_person_properties_request = SetPersonPropertiesRequest.from_dict({})
        set_person_properties_request = SetPersonPropertiesRequest()

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.set_person_properties(id_type_scope, id_type_code, code, set_person_properties_request, opts=opts)

            # [EARLY ACCESS] SetPersonProperties: Set Person Properties
            api_response = await api_instance.set_person_properties(id_type_scope, id_type_code, code, set_person_properties_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling PersonsApi->set_person_properties: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_type_scope** | **str**| Scope of the person identifier type. | 
 **id_type_code** | **str**| Code of the person identifier type. | 
 **code** | **str**| Code of the person under specified identifier type&#39;s scope and code. This together with stated identifier type uniquely              identifies the person. | 
 **set_person_properties_request** | [**SetPersonPropertiesRequest**](SetPersonPropertiesRequest.md)| Request containing properties to set for the person. Properties not specified in request will not be changed. | 

### Return type

[**Person**](Person.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Person with updated properties or identifiers. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **upsert_person**
> Person upsert_person(upsert_person_request)

UpsertPerson: Upsert Person

Create or update a new person under the specified scope.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    PersonsApi
)

async def main():

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

    # Use the lusid ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(PersonsApi)

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # upsert_person_request = UpsertPersonRequest.from_json("")
        # upsert_person_request = UpsertPersonRequest.from_dict({})
        upsert_person_request = UpsertPersonRequest()

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.upsert_person(upsert_person_request, opts=opts)

            # UpsertPerson: Upsert Person
            api_response = await api_instance.upsert_person(upsert_person_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling PersonsApi->upsert_person: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_person_request** | [**UpsertPersonRequest**](UpsertPersonRequest.md)| Request to create or update a person. | 

### Return type

[**Person**](Person.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created or updated person |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **upsert_person_access_metadata**
> ResourceListOfAccessMetadataValueOf upsert_person_access_metadata(id_type_scope, id_type_code, code, metadata_key, upsert_person_access_metadata_request, effective_at=effective_at, effective_until=effective_until)

[EARLY ACCESS] UpsertPersonAccessMetadata: Upsert a Person Access Metadata entry associated with a specific metadataKey. This creates or updates the data in LUSID.

Update or insert one Person Access Metadata entry in a single scope. An item will be updated if it already exists  and inserted if it does not.                The response will return the successfully updated or inserted Person Access Metadata rule or failure message if unsuccessful.                It is important to always check to verify success (or failure).                Multiple rules for a metadataKey can exist with different effective at dates, when resources are accessed the rule that is active for the current time will be fetched.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    PersonsApi
)

async def main():

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

    # Use the lusid ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(PersonsApi)
        id_type_scope = 'id_type_scope_example' # str | Scope of the person identifier.
        id_type_code = 'id_type_code_example' # str | Code of the person identifier.
        code = 'code_example' # str | Code of the person under specified identifier type's scope and code.
        metadata_key = 'metadata_key_example' # str | Key of the metadata entry to retrieve

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # upsert_person_access_metadata_request = UpsertPersonAccessMetadataRequest.from_json("")
        # upsert_person_access_metadata_request = UpsertPersonAccessMetadataRequest.from_dict({})
        upsert_person_access_metadata_request = UpsertPersonAccessMetadataRequest()
        effective_at = 'effective_at_example' # str | The effectiveAt datetime at which to upsert the Access Metadata (optional)
        effective_until = '2013-10-20T19:20:30+01:00' # datetime | The effective datetime until which the Access Metadata is valid. If not supplied this will be valid indefinitely, or until the next 'effectiveAt' datetime of the Access Metadata (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.upsert_person_access_metadata(id_type_scope, id_type_code, code, metadata_key, upsert_person_access_metadata_request, effective_at=effective_at, effective_until=effective_until, opts=opts)

            # [EARLY ACCESS] UpsertPersonAccessMetadata: Upsert a Person Access Metadata entry associated with a specific metadataKey. This creates or updates the data in LUSID.
            api_response = await api_instance.upsert_person_access_metadata(id_type_scope, id_type_code, code, metadata_key, upsert_person_access_metadata_request, effective_at=effective_at, effective_until=effective_until)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling PersonsApi->upsert_person_access_metadata: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_type_scope** | **str**| Scope of the person identifier. | 
 **id_type_code** | **str**| Code of the person identifier. | 
 **code** | **str**| Code of the person under specified identifier type&#39;s scope and code. | 
 **metadata_key** | **str**| Key of the metadata entry to retrieve | 
 **upsert_person_access_metadata_request** | [**UpsertPersonAccessMetadataRequest**](UpsertPersonAccessMetadataRequest.md)| The Person Access Metadata entry to upsert | 
 **effective_at** | **str**| The effectiveAt datetime at which to upsert the Access Metadata | [optional] 
 **effective_until** | **datetime**| The effective datetime until which the Access Metadata is valid. If not supplied this will be valid indefinitely, or until the next &#39;effectiveAt&#39; datetime of the Access Metadata | [optional] 

### Return type

[**ResourceListOfAccessMetadataValueOf**](ResourceListOfAccessMetadataValueOf.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully updated or inserted item or any failure. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **upsert_persons**
> UpsertPersonsResponse upsert_persons(success_mode, request_body)

[EARLY ACCESS] UpsertPersons: Pluralised Upsert of Persons

Create or updates a collection of person(s).

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    PersonsApi
)

async def main():

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

    # Use the lusid ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(PersonsApi)
        success_mode = 'success_mode_example' # str | Whether the batch request should fail Atomically or in a Partial fashion - Allowed Values: Atomic, Partial
        request_body = {"firstPersonExample":{"identifiers":{"Person/HrSystem1/InternalId":{"key":"Person/HrSystem1/InternalId","value":{"labelValue":"XY10001111"}},"Person/PayrollSystem1/Id":{"key":"Person/PayrollSystem1/Id","value":{"labelValue":"HSI3453456"}},"Person/CompanyIntranet/LoginId":{"key":"Person/CompanyIntranet/LoginId","value":{"labelValue":"johnsmith001"}}},"properties":{"Person/PersonalDetails/Name":{"key":"Person/PersonalDetails/Name","value":{"labelValue":"John Smith"}},"Person/CompanyDetails/Role":{"key":"Person/CompanyDetails/Role","value":{"labelValueSet":{"values":["SalesRepresentative","CustomerServiceRepresentative"]}},"effectiveFrom":"2016-07-01T00:00:00.0000000+00:00"}},"displayName":"Person1DisplayName","description":"Person1Description"},"secondPersonExample":{"identifiers":{"Person/HrSystem1/InternalId":{"key":"Person/HrSystem1/InternalId","value":{"labelValue":"XY10008377"}},"Person/PayrollSystem1/Id":{"key":"Person/PayrollSystem1/Id","value":{"labelValue":"LFK9172001"}},"Person/CompanyIntranet/LoginId":{"key":"Person/CompanyIntranet/LoginId","value":{"labelValue":"emilyevans002"}}},"properties":{"Person/PersonalDetails/Name":{"key":"Person/PersonalDetails/Name","value":{"labelValue":"Emily Evans"}},"Person/ContactDetails/Phone":{"key":"Person/ContactDetails/Phone","value":{"labelValue":"01005675678"}},"Person/CompanyDetails/Role":{"key":"Person/CompanyDetails/Role","value":{"labelValue":"Manager"},"effectiveFrom":"2018-04-01T00:00:00.0000000+00:00"}},"displayName":"Person2DisplayName","description":"Person2Description"}} # Dict[str, UpsertPersonRequest] | A collection of requests to create or update Person(s).

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.upsert_persons(success_mode, request_body, opts=opts)

            # [EARLY ACCESS] UpsertPersons: Pluralised Upsert of Persons
            api_response = await api_instance.upsert_persons(success_mode, request_body)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling PersonsApi->upsert_persons: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **success_mode** | **str**| Whether the batch request should fail Atomically or in a Partial fashion - Allowed Values: Atomic, Partial | 
 **request_body** | [**Dict[str, UpsertPersonRequest]**](UpsertPersonRequest.md)| A collection of requests to create or update Person(s). | 

### Return type

[**UpsertPersonsResponse**](UpsertPersonsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created or updated person(s) |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

