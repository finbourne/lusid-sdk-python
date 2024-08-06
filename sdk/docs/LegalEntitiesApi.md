# lusid.LegalEntitiesApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_legal_entity**](LegalEntitiesApi.md#delete_legal_entity) | **DELETE** /api/legalentities/{idTypeScope}/{idTypeCode}/{code} | DeleteLegalEntity: Delete Legal Entity
[**delete_legal_entity_access_metadata**](LegalEntitiesApi.md#delete_legal_entity_access_metadata) | **DELETE** /api/legalentities/{idTypeScope}/{idTypeCode}/{code}/metadata/{metadataKey} | [EARLY ACCESS] DeleteLegalEntityAccessMetadata: Delete a Legal Entity Access Metadata entry
[**delete_legal_entity_identifiers**](LegalEntitiesApi.md#delete_legal_entity_identifiers) | **DELETE** /api/legalentities/{idTypeScope}/{idTypeCode}/{code}/identifiers | [EARLY ACCESS] DeleteLegalEntityIdentifiers: Delete Legal Entity Identifiers
[**delete_legal_entity_properties**](LegalEntitiesApi.md#delete_legal_entity_properties) | **DELETE** /api/legalentities/{idTypeScope}/{idTypeCode}/{code}/properties | [EARLY ACCESS] DeleteLegalEntityProperties: Delete Legal Entity Properties
[**get_all_legal_entity_access_metadata**](LegalEntitiesApi.md#get_all_legal_entity_access_metadata) | **GET** /api/legalentities/{idTypeScope}/{idTypeCode}/{code}/metadata | GetAllLegalEntityAccessMetadata: Get Access Metadata rules for a Legal Entity
[**get_legal_entity**](LegalEntitiesApi.md#get_legal_entity) | **GET** /api/legalentities/{idTypeScope}/{idTypeCode}/{code} | GetLegalEntity: Get Legal Entity
[**get_legal_entity_access_metadata_by_key**](LegalEntitiesApi.md#get_legal_entity_access_metadata_by_key) | **GET** /api/legalentities/{idTypeScope}/{idTypeCode}/{code}/metadata/{metadataKey} | [EARLY ACCESS] GetLegalEntityAccessMetadataByKey: Get an entry identified by a metadataKey in the Access Metadata of a Legal Entity
[**get_legal_entity_property_time_series**](LegalEntitiesApi.md#get_legal_entity_property_time_series) | **GET** /api/legalentities/{idTypeScope}/{idTypeCode}/{code}/properties/time-series | GetLegalEntityPropertyTimeSeries: Get Legal Entity Property Time Series
[**get_legal_entity_relations**](LegalEntitiesApi.md#get_legal_entity_relations) | **GET** /api/legalentities/{idTypeScope}/{idTypeCode}/{code}/relations | GetLegalEntityRelations: Get Relations for Legal Entity
[**get_legal_entity_relationships**](LegalEntitiesApi.md#get_legal_entity_relationships) | **GET** /api/legalentities/{idTypeScope}/{idTypeCode}/{code}/relationships | GetLegalEntityRelationships: Get Relationships for Legal Entity
[**list_all_legal_entities**](LegalEntitiesApi.md#list_all_legal_entities) | **GET** /api/legalentities | ListAllLegalEntities: List Legal Entities
[**list_legal_entities**](LegalEntitiesApi.md#list_legal_entities) | **GET** /api/legalentities/{idTypeScope}/{idTypeCode} | ListLegalEntities: List Legal Entities
[**patch_legal_entity_access_metadata**](LegalEntitiesApi.md#patch_legal_entity_access_metadata) | **PATCH** /api/legalentities/{idTypeScope}/{idTypeCode}/{code}/metadata | [EARLY ACCESS] PatchLegalEntityAccessMetadata: Patch Access Metadata rules for a Legal Entity.
[**set_legal_entity_identifiers**](LegalEntitiesApi.md#set_legal_entity_identifiers) | **POST** /api/legalentities/{idTypeScope}/{idTypeCode}/{code}/identifiers | [EARLY ACCESS] SetLegalEntityIdentifiers: Set Legal Entity Identifiers
[**set_legal_entity_properties**](LegalEntitiesApi.md#set_legal_entity_properties) | **POST** /api/legalentities/{idTypeScope}/{idTypeCode}/{code}/properties | SetLegalEntityProperties: Set Legal Entity Properties
[**upsert_legal_entities**](LegalEntitiesApi.md#upsert_legal_entities) | **POST** /api/legalentities/$batchUpsert | [EARLY ACCESS] UpsertLegalEntities: Pluralised upsert of Legal Entities
[**upsert_legal_entity**](LegalEntitiesApi.md#upsert_legal_entity) | **POST** /api/legalentities | UpsertLegalEntity: Upsert Legal Entity
[**upsert_legal_entity_access_metadata**](LegalEntitiesApi.md#upsert_legal_entity_access_metadata) | **PUT** /api/legalentities/{idTypeScope}/{idTypeCode}/{code}/metadata/{metadataKey} | [EARLY ACCESS] UpsertLegalEntityAccessMetadata: Upsert a Legal Entity Access Metadata entry associated with a specific metadataKey. This creates or updates the data in LUSID.


# **delete_legal_entity**
> DeletedEntityResponse delete_legal_entity(id_type_scope, id_type_code, code)

DeleteLegalEntity: Delete Legal Entity

Delete a legal entity. Deletion will be valid from the legal entity's creation datetime.  This means that the legal entity will no longer exist at any effective datetime from the asAt datetime of deletion.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    LegalEntitiesApi
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
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(LegalEntitiesApi)
        id_type_scope = 'id_type_scope_example' # str | The scope of the legal entity identifier type.
        id_type_code = 'id_type_code_example' # str | The code of the legal entity identifier type.
        code = 'code_example' # str | Code of the legal entity under specified identifier type's scope and code. This together with defined              identifier type uniquely identifies the legal entity to delete.

        try:
            # DeleteLegalEntity: Delete Legal Entity
            api_response = await api_instance.delete_legal_entity(id_type_scope, id_type_code, code)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling LegalEntitiesApi->delete_legal_entity: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_type_scope** | **str**| The scope of the legal entity identifier type. | 
 **id_type_code** | **str**| The code of the legal entity identifier type. | 
 **code** | **str**| Code of the legal entity under specified identifier type&#39;s scope and code. This together with defined              identifier type uniquely identifies the legal entity to delete. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response from deleting legal entity. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_legal_entity_access_metadata**
> DeletedEntityResponse delete_legal_entity_access_metadata(id_type_scope, id_type_code, code, metadata_key, effective_at=effective_at, effective_until=effective_until)

[EARLY ACCESS] DeleteLegalEntityAccessMetadata: Delete a Legal Entity Access Metadata entry

Deletes the Legal Entity Access Metadata entry that exactly matches the provided identifier parts.    It is important to always check to verify success (or failure).

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    LegalEntitiesApi
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
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(LegalEntitiesApi)
        id_type_scope = 'id_type_scope_example' # str | Scope of the Legal Entity identifier.
        id_type_code = 'id_type_code_example' # str | Code of the Legal Entity identifier.
        code = 'code_example' # str | Code of the Legal Entity under specified identifier type's scope and code.
        metadata_key = 'metadata_key_example' # str | Key of the metadata entry to retrieve
        effective_at = 'effective_at_example' # str | The effective date to delete at, if this is not supplied, it will delete all data found (optional)
        effective_until = '2013-10-20T19:20:30+01:00' # datetime | The effective date until which the delete is valid. If not supplied this will be valid indefinitely, or until the next 'effectiveAt' date of the Access Metadata (optional)

        try:
            # [EARLY ACCESS] DeleteLegalEntityAccessMetadata: Delete a Legal Entity Access Metadata entry
            api_response = await api_instance.delete_legal_entity_access_metadata(id_type_scope, id_type_code, code, metadata_key, effective_at=effective_at, effective_until=effective_until)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling LegalEntitiesApi->delete_legal_entity_access_metadata: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_type_scope** | **str**| Scope of the Legal Entity identifier. | 
 **id_type_code** | **str**| Code of the Legal Entity identifier. | 
 **code** | **str**| Code of the Legal Entity under specified identifier type&#39;s scope and code. | 
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

# **delete_legal_entity_identifiers**
> DeletedEntityResponse delete_legal_entity_identifiers(id_type_scope, id_type_code, code, property_keys, effective_at=effective_at)

[EARLY ACCESS] DeleteLegalEntityIdentifiers: Delete Legal Entity Identifiers

Delete identifiers that belong to the given property keys of the legal entity.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    LegalEntitiesApi
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
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(LegalEntitiesApi)
        id_type_scope = 'id_type_scope_example' # str | Scope of the legal entity identifier type.
        id_type_code = 'id_type_code_example' # str | Code of the legal entity identifier type.
        code = 'code_example' # str | Code of the legal entity under specified identifier type's scope and code. This together with stated identifier type uniquely              identifies the legal entity.
        property_keys = ['property_keys_example'] # List[str] | The property keys of the identifiers to delete. These take the format              {domain}/{scope}/{code} e.g. \"LegalEntity/CreditAgency/Identifier\". Each property must be from the \"LegalEntity\" domain. Identifiers or identifiers not specified in request will not be changed.
        effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to delete the identifiers. Defaults to the current LUSID system datetime if not specified.              Must not include an effective datetime if identifiers are perpetual. (optional)

        try:
            # [EARLY ACCESS] DeleteLegalEntityIdentifiers: Delete Legal Entity Identifiers
            api_response = await api_instance.delete_legal_entity_identifiers(id_type_scope, id_type_code, code, property_keys, effective_at=effective_at)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling LegalEntitiesApi->delete_legal_entity_identifiers: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_type_scope** | **str**| Scope of the legal entity identifier type. | 
 **id_type_code** | **str**| Code of the legal entity identifier type. | 
 **code** | **str**| Code of the legal entity under specified identifier type&#39;s scope and code. This together with stated identifier type uniquely              identifies the legal entity. | 
 **property_keys** | [**List[str]**](str.md)| The property keys of the identifiers to delete. These take the format              {domain}/{scope}/{code} e.g. \&quot;LegalEntity/CreditAgency/Identifier\&quot;. Each property must be from the \&quot;LegalEntity\&quot; domain. Identifiers or identifiers not specified in request will not be changed. | 
 **effective_at** | **str**| The effective datetime or cut label at which to delete the identifiers. Defaults to the current LUSID system datetime if not specified.              Must not include an effective datetime if identifiers are perpetual. | [optional] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the identifiers were deleted from the specified legal entity |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_legal_entity_properties**
> DeletedEntityResponse delete_legal_entity_properties(id_type_scope, id_type_code, code, property_keys, effective_at=effective_at)

[EARLY ACCESS] DeleteLegalEntityProperties: Delete Legal Entity Properties

Delete all properties that belong to the given property keys of the legal entity.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    LegalEntitiesApi
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
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(LegalEntitiesApi)
        id_type_scope = 'id_type_scope_example' # str | Scope of the legal entity identifier type.
        id_type_code = 'id_type_code_example' # str | Code of the legal entity identifier type.
        code = 'code_example' # str | Code of the legal entity under specified identifier type's scope and code. This together with stated identifier type uniquely              identifies the legal entity.
        property_keys = ['property_keys_example'] # List[str] | The property keys of the legal entities properties to delete. These take the format              {domain}/{scope}/{code} e.g. \"LegalEntity/CompanyDetails/Role\". Each property must be from the \"LegalEntity\" domain. Properties or identifiers not specified in request will not be changed.
        effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to delete time-variant properties from.              The property must exist at the specified 'effectiveAt' datetime. If the 'effectiveAt' is not provided or is              before the time-variant property exists then a failure is returned. Do not specify this parameter if any of              the properties to delete are perpetual. (optional)

        try:
            # [EARLY ACCESS] DeleteLegalEntityProperties: Delete Legal Entity Properties
            api_response = await api_instance.delete_legal_entity_properties(id_type_scope, id_type_code, code, property_keys, effective_at=effective_at)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling LegalEntitiesApi->delete_legal_entity_properties: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_type_scope** | **str**| Scope of the legal entity identifier type. | 
 **id_type_code** | **str**| Code of the legal entity identifier type. | 
 **code** | **str**| Code of the legal entity under specified identifier type&#39;s scope and code. This together with stated identifier type uniquely              identifies the legal entity. | 
 **property_keys** | [**List[str]**](str.md)| The property keys of the legal entities properties to delete. These take the format              {domain}/{scope}/{code} e.g. \&quot;LegalEntity/CompanyDetails/Role\&quot;. Each property must be from the \&quot;LegalEntity\&quot; domain. Properties or identifiers not specified in request will not be changed. | 
 **effective_at** | **str**| The effective datetime or cut label at which to delete time-variant properties from.              The property must exist at the specified &#39;effectiveAt&#39; datetime. If the &#39;effectiveAt&#39; is not provided or is              before the time-variant property exists then a failure is returned. Do not specify this parameter if any of              the properties to delete are perpetual. | [optional] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the properties were deleted from the specified legal entity |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_all_legal_entity_access_metadata**
> Dict[str, List[AccessMetadataValue]] get_all_legal_entity_access_metadata(id_type_scope, id_type_code, code, effective_at=effective_at, as_at=as_at)

GetAllLegalEntityAccessMetadata: Get Access Metadata rules for a Legal Entity

Pass the Scope and Code of the Legal Entity identifier along with the Legal Entity code parameter to retrieve the associated Access Metadata

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    LegalEntitiesApi
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
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(LegalEntitiesApi)
        id_type_scope = 'id_type_scope_example' # str | Scope of the Legal Entity identifier.
        id_type_code = 'id_type_code_example' # str | Code of the Legal Entity identifier.
        code = 'code_example' # str | Code of the Legal Entity under specified identifier type's scope and code.
        effective_at = 'effective_at_example' # str | The effectiveAt datetime at which to retrieve the Access Metadata (optional)
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Access Metadata (optional)

        try:
            # GetAllLegalEntityAccessMetadata: Get Access Metadata rules for a Legal Entity
            api_response = await api_instance.get_all_legal_entity_access_metadata(id_type_scope, id_type_code, code, effective_at=effective_at, as_at=as_at)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling LegalEntitiesApi->get_all_legal_entity_access_metadata: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_type_scope** | **str**| Scope of the Legal Entity identifier. | 
 **id_type_code** | **str**| Code of the Legal Entity identifier. | 
 **code** | **str**| Code of the Legal Entity under specified identifier type&#39;s scope and code. | 
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
**200** | The access metadata for the Legal Entity or any failure. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_legal_entity**
> LegalEntity get_legal_entity(id_type_scope, id_type_code, code, property_keys=property_keys, effective_at=effective_at, as_at=as_at, relationship_definition_ids=relationship_definition_ids)

GetLegalEntity: Get Legal Entity

Retrieve the definition of a legal entity.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    LegalEntitiesApi
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
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(LegalEntitiesApi)
        id_type_scope = 'id_type_scope_example' # str | Scope of the legal entity identifier type.
        id_type_code = 'id_type_code_example' # str | Code of the legal entity identifier type.
        code = 'code_example' # str | Code of the legal entity under specified identifier type's scope and code. This together with stated identifier type uniquely              identifies the legal entity.
        property_keys = ['property_keys_example'] # List[str] | A list of property keys or identifier types (as property keys) from the \"LegalEntity\" domain              to include for found legal entity, or from any domain that supports relationships to decorate onto related entities.              These take the format {domain}/{scope}/{code} e.g. \"LegalEntity/ContactDetails/Address\". (optional)
        effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the legal entity. Defaults to the current LUSID system datetime if not specified. (optional)
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the legal entity. Defaults to return the latest version of the legal entity if not specified. (optional)
        relationship_definition_ids = ['relationship_definition_ids_example'] # List[str] | A list of relationship definitions that are used to decorate related entities              onto the legal entity in the response. These must take the form {relationshipDefinitionScope}/{relationshipDefinitionCode}. (optional)

        try:
            # GetLegalEntity: Get Legal Entity
            api_response = await api_instance.get_legal_entity(id_type_scope, id_type_code, code, property_keys=property_keys, effective_at=effective_at, as_at=as_at, relationship_definition_ids=relationship_definition_ids)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling LegalEntitiesApi->get_legal_entity: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_type_scope** | **str**| Scope of the legal entity identifier type. | 
 **id_type_code** | **str**| Code of the legal entity identifier type. | 
 **code** | **str**| Code of the legal entity under specified identifier type&#39;s scope and code. This together with stated identifier type uniquely              identifies the legal entity. | 
 **property_keys** | [**List[str]**](str.md)| A list of property keys or identifier types (as property keys) from the \&quot;LegalEntity\&quot; domain              to include for found legal entity, or from any domain that supports relationships to decorate onto related entities.              These take the format {domain}/{scope}/{code} e.g. \&quot;LegalEntity/ContactDetails/Address\&quot;. | [optional] 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the legal entity. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the legal entity. Defaults to return the latest version of the legal entity if not specified. | [optional] 
 **relationship_definition_ids** | [**List[str]**](str.md)| A list of relationship definitions that are used to decorate related entities              onto the legal entity in the response. These must take the form {relationshipDefinitionScope}/{relationshipDefinitionCode}. | [optional] 

### Return type

[**LegalEntity**](LegalEntity.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested legal entity |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_legal_entity_access_metadata_by_key**
> List[AccessMetadataValue] get_legal_entity_access_metadata_by_key(id_type_scope, id_type_code, code, metadata_key, effective_at=effective_at, as_at=as_at)

[EARLY ACCESS] GetLegalEntityAccessMetadataByKey: Get an entry identified by a metadataKey in the Access Metadata of a Legal Entity

Get a specific Legal Entity Access Metadata by specifying the corresponding identifier parts and Legal Entity code                No matching will be performed through this endpoint. To retrieve an entry, it is necessary to specify, exactly, the identifier of the entry

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    LegalEntitiesApi
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
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(LegalEntitiesApi)
        id_type_scope = 'id_type_scope_example' # str | Scope of the Legal Entity identifier.
        id_type_code = 'id_type_code_example' # str | Code of the Legal Entity identifier.
        code = 'code_example' # str | Code of the Legal Entity under specified identifier type's scope and code.
        metadata_key = 'metadata_key_example' # str | Key of the metadata entry to retrieve
        effective_at = 'effective_at_example' # str | The effectiveAt datetime at which to retrieve the Access Metadata (optional)
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Access Metadata (optional)

        try:
            # [EARLY ACCESS] GetLegalEntityAccessMetadataByKey: Get an entry identified by a metadataKey in the Access Metadata of a Legal Entity
            api_response = await api_instance.get_legal_entity_access_metadata_by_key(id_type_scope, id_type_code, code, metadata_key, effective_at=effective_at, as_at=as_at)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling LegalEntitiesApi->get_legal_entity_access_metadata_by_key: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_type_scope** | **str**| Scope of the Legal Entity identifier. | 
 **id_type_code** | **str**| Code of the Legal Entity identifier. | 
 **code** | **str**| Code of the Legal Entity under specified identifier type&#39;s scope and code. | 
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
**200** | The successfully retrieved Legal Entity access metadata filtered by metadataKey or any failure. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_legal_entity_property_time_series**
> ResourceListOfPropertyInterval get_legal_entity_property_time_series(id_type_scope, id_type_code, code, property_key, as_at=as_at, filter=filter, page=page, limit=limit)

GetLegalEntityPropertyTimeSeries: Get Legal Entity Property Time Series

List the complete time series of a legal entity property.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    LegalEntitiesApi
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
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(LegalEntitiesApi)
        id_type_scope = 'id_type_scope_example' # str | Scope of the legal entity identifier type.
        id_type_code = 'id_type_code_example' # str | Code of the legal entity identifier type.
        code = 'code_example' # str | Code of the legal entity under specified identifier type's scope and code. This together with stated identifier type uniquely identifies the legal entity.
        property_key = 'property_key_example' # str | The property key of the property that will have its history shown. These must be in the format {domain}/{scope}/{code} e.g. \"LegalEntity/ContactDetails/Address\".              Each property must be from the \"LegalEntity\" domain.
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the person's property history. Defaults to return the current datetime if not supplied. (optional)
        filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)
        page = 'page_example' # str | The pagination token to use to continue listing properties from a previous call to get property time series.              This value is returned from the previous call. If a pagination token is provided the filter and asAt fields              must not have changed since the original request. (optional)
        limit = 56 # int | When paginating, limit the number of returned results to this many. (optional)

        try:
            # GetLegalEntityPropertyTimeSeries: Get Legal Entity Property Time Series
            api_response = await api_instance.get_legal_entity_property_time_series(id_type_scope, id_type_code, code, property_key, as_at=as_at, filter=filter, page=page, limit=limit)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling LegalEntitiesApi->get_legal_entity_property_time_series: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_type_scope** | **str**| Scope of the legal entity identifier type. | 
 **id_type_code** | **str**| Code of the legal entity identifier type. | 
 **code** | **str**| Code of the legal entity under specified identifier type&#39;s scope and code. This together with stated identifier type uniquely identifies the legal entity. | 
 **property_key** | **str**| The property key of the property that will have its history shown. These must be in the format {domain}/{scope}/{code} e.g. \&quot;LegalEntity/ContactDetails/Address\&quot;.              Each property must be from the \&quot;LegalEntity\&quot; domain. | 
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

# **get_legal_entity_relations**
> ResourceListOfRelation get_legal_entity_relations(id_type_scope, id_type_code, code, effective_at=effective_at, as_at=as_at, filter=filter, identifier_types=identifier_types)

GetLegalEntityRelations: Get Relations for Legal Entity

Get relations for the specified Legal Entity

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    LegalEntitiesApi
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
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(LegalEntitiesApi)
        id_type_scope = 'id_type_scope_example' # str | Scope of the legal entity identifier type.
        id_type_code = 'id_type_code_example' # str | Code of the legal entity identifier type.
        code = 'code_example' # str | Code of the legal entity under specified identifier type's scope and code. This together with stated identifier type uniquely              identifies the legal entity.
        effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to get relations. Defaults to the current LUSID system datetime if not specified. (optional)
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the legal entity's relations. Defaults to return the latest LUSID AsAt time if not specified. (optional)
        filter = 'filter_example' # str | Expression to filter the relations. Users should provide null or empty string for this field until further notice. (optional)
        identifier_types = ['identifier_types_example'] # List[str] | Identifiers types (as property keys) used for referencing Persons or Legal Entities. These take the format              {domain}/{scope}/{code} e.g. \"Person/CompanyDetails/Role\". They must be from the \"Person\" or \"LegalEntity\" domain.              Only identifier types stated will be used to look up relevant entities in relations. If not applicable, provide an empty array. (optional)

        try:
            # GetLegalEntityRelations: Get Relations for Legal Entity
            api_response = await api_instance.get_legal_entity_relations(id_type_scope, id_type_code, code, effective_at=effective_at, as_at=as_at, filter=filter, identifier_types=identifier_types)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling LegalEntitiesApi->get_legal_entity_relations: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_type_scope** | **str**| Scope of the legal entity identifier type. | 
 **id_type_code** | **str**| Code of the legal entity identifier type. | 
 **code** | **str**| Code of the legal entity under specified identifier type&#39;s scope and code. This together with stated identifier type uniquely              identifies the legal entity. | 
 **effective_at** | **str**| The effective datetime or cut label at which to get relations. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the legal entity&#39;s relations. Defaults to return the latest LUSID AsAt time if not specified. | [optional] 
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
**200** | The relations for the specific legal entity. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_legal_entity_relationships**
> ResourceListOfRelationship get_legal_entity_relationships(id_type_scope, id_type_code, code, effective_at=effective_at, as_at=as_at, filter=filter, identifier_types=identifier_types)

GetLegalEntityRelationships: Get Relationships for Legal Entity

Get Relationships for the specified Legal Entity

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    LegalEntitiesApi
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
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(LegalEntitiesApi)
        id_type_scope = 'id_type_scope_example' # str | Scope of the legal entity's identifier type.
        id_type_code = 'id_type_code_example' # str | Code of the legal entity's identifier type.
        code = 'code_example' # str | Code of the legal entity under specified identifier type's scope and code. This together with stated identifier type uniquely              identifies the legal entity.
        effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to get relationships. Defaults to the current LUSID system datetime if not specified. (optional)
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve relationships. Defaults to return the latest LUSID AsAt time if not specified. (optional)
        filter = 'filter_example' # str | Expression to filter relationships. Users should provide null or empty string for this field until further notice. (optional)
        identifier_types = ['identifier_types_example'] # List[str] | Identifier types (as property keys) used for referencing Persons or Legal Entities.              These can be specified from the 'Person' or 'LegalEntity' domains and have the format {domain}/{scope}/{code}, for example              'Person/CompanyDetails/Role'. An Empty array may be used to return all related Entities. (optional)

        try:
            # GetLegalEntityRelationships: Get Relationships for Legal Entity
            api_response = await api_instance.get_legal_entity_relationships(id_type_scope, id_type_code, code, effective_at=effective_at, as_at=as_at, filter=filter, identifier_types=identifier_types)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling LegalEntitiesApi->get_legal_entity_relationships: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_type_scope** | **str**| Scope of the legal entity&#39;s identifier type. | 
 **id_type_code** | **str**| Code of the legal entity&#39;s identifier type. | 
 **code** | **str**| Code of the legal entity under specified identifier type&#39;s scope and code. This together with stated identifier type uniquely              identifies the legal entity. | 
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
**200** | The relationships for the specified legal entity. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_all_legal_entities**
> ResourceListOfLegalEntity list_all_legal_entities(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys, relationship_definition_ids=relationship_definition_ids)

ListAllLegalEntities: List Legal Entities

List all legal entities which the user is entitled to see.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    LegalEntitiesApi
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
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(LegalEntitiesApi)
        effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to list the legal entities. Defaults to the current LUSID              system datetime if not specified. (optional)
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the legal entities. Defaults to return the latest version              of each legal entities if not specified. (optional)
        page = 'page_example' # str | The pagination token to use to continue listing legal entities from a previous call to list legal entities. This  value is returned from the previous call. If a pagination token is provided the filter, effectiveAt, sortBy  and asAt fields must not have changed since the original request. (optional)
        limit = 56 # int | When paginating, limit the number of returned results to this many. Defaults to 5000 if not specified. (optional)
        filter = 'filter_example' # str | Expression to filter the result set.               Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)
        sort_by = ['sort_by_example'] # List[str] | A list of field names or properties to sort by, each suffixed by \" ASC\" or \" DESC\". (optional)
        property_keys = ['property_keys_example'] # List[str] | A list of property keys or identifier types (as property keys) from the \"LegalEntity\" domain              to include for each legal entity, or from any domain that supports relationships to decorate onto related entities.              These take the format {domain}/{scope}/{code} e.g. \"LegalEntity/ContactDetails/Address\". (optional)
        relationship_definition_ids = ['relationship_definition_ids_example'] # List[str] | A list of relationship definitions that are used to decorate related entities              onto each portfolio in the response. These must take the form {relationshipDefinitionScope}/{relationshipDefinitionCode}. (optional)

        try:
            # ListAllLegalEntities: List Legal Entities
            api_response = await api_instance.list_all_legal_entities(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys, relationship_definition_ids=relationship_definition_ids)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling LegalEntitiesApi->list_all_legal_entities: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **effective_at** | **str**| The effective datetime or cut label at which to list the legal entities. Defaults to the current LUSID              system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the legal entities. Defaults to return the latest version              of each legal entities if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing legal entities from a previous call to list legal entities. This  value is returned from the previous call. If a pagination token is provided the filter, effectiveAt, sortBy  and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 5000 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set.               Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys or identifier types (as property keys) from the \&quot;LegalEntity\&quot; domain              to include for each legal entity, or from any domain that supports relationships to decorate onto related entities.              These take the format {domain}/{scope}/{code} e.g. \&quot;LegalEntity/ContactDetails/Address\&quot;. | [optional] 
 **relationship_definition_ids** | [**List[str]**](str.md)| A list of relationship definitions that are used to decorate related entities              onto each portfolio in the response. These must take the form {relationshipDefinitionScope}/{relationshipDefinitionCode}. | [optional] 

### Return type

[**ResourceListOfLegalEntity**](ResourceListOfLegalEntity.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All existing Legal Entities |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_legal_entities**
> PagedResourceListOfLegalEntity list_legal_entities(id_type_scope, id_type_code, effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys, relationship_definition_ids=relationship_definition_ids)

ListLegalEntities: List Legal Entities

List legal entities which has identifier of specific identifier type's scope and code, and satisfies filter criteria.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    LegalEntitiesApi
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
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(LegalEntitiesApi)
        id_type_scope = 'id_type_scope_example' # str | Scope of the legal entity identifier type.
        id_type_code = 'id_type_code_example' # str | Code of the legal entity identifier type.
        effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to list the people. Defaults to the current LUSID              system datetime if not specified. (optional)
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the people. Defaults to return the latest version              of each people if not specified. (optional)
        page = 'page_example' # str | The pagination token to use to continue listing legal entities from a previous call to list legal entities. This  value is returned from the previous call. If a pagination token is provided the filter, effectiveAt, sortBy  and asAt fields must not have changed since the original request. (optional)
        limit = 56 # int | When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. (optional)
        filter = 'filter_example' # str | Expression to filter the result set.               Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)
        sort_by = ['sort_by_example'] # List[str] | A list of field names or properties to sort by, each suffixed by \" ASC\" or \" DESC\". (optional)
        property_keys = ['property_keys_example'] # List[str] | A list of property keys or identifier types (as property keys) from the \"LegalEntity\" domain              to include for each legal entity, or from any domain that supports relationships to decorate onto related entities.              These take the format {domain}/{scope}/{code} e.g. \"LegalEntity/ContactDetails/Address\". (optional)
        relationship_definition_ids = ['relationship_definition_ids_example'] # List[str] | A list of relationship definitions that are used to decorate related entities              onto each portfolio in the response. These must take the form {relationshipDefinitionScope}/{relationshipDefinitionCode}. (optional)

        try:
            # ListLegalEntities: List Legal Entities
            api_response = await api_instance.list_legal_entities(id_type_scope, id_type_code, effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys, relationship_definition_ids=relationship_definition_ids)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling LegalEntitiesApi->list_legal_entities: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_type_scope** | **str**| Scope of the legal entity identifier type. | 
 **id_type_code** | **str**| Code of the legal entity identifier type. | 
 **effective_at** | **str**| The effective datetime or cut label at which to list the people. Defaults to the current LUSID              system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the people. Defaults to return the latest version              of each people if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing legal entities from a previous call to list legal entities. This  value is returned from the previous call. If a pagination token is provided the filter, effectiveAt, sortBy  and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set.               Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys or identifier types (as property keys) from the \&quot;LegalEntity\&quot; domain              to include for each legal entity, or from any domain that supports relationships to decorate onto related entities.              These take the format {domain}/{scope}/{code} e.g. \&quot;LegalEntity/ContactDetails/Address\&quot;. | [optional] 
 **relationship_definition_ids** | [**List[str]**](str.md)| A list of relationship definitions that are used to decorate related entities              onto each portfolio in the response. These must take the form {relationshipDefinitionScope}/{relationshipDefinitionCode}. | [optional] 

### Return type

[**PagedResourceListOfLegalEntity**](PagedResourceListOfLegalEntity.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Legal Entities with specified identifier type |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **patch_legal_entity_access_metadata**
> Dict[str, List[AccessMetadataValue]] patch_legal_entity_access_metadata(id_type_scope, id_type_code, code, access_metadata_operation, effective_at=effective_at, effective_until=effective_until)

[EARLY ACCESS] PatchLegalEntityAccessMetadata: Patch Access Metadata rules for a Legal Entity.

Patch Legal Entity Access Metadata Rules in a single scope.  The behaviour is defined by the JSON Patch specification.                Currently only 'add' is a supported operation on the patch document    Currently only valid metadata keys are supported paths on the patch document                The response will return any affected Legal Entity Access Metadata rules or a failure message if unsuccessful.                It is important to always check to verify success (or failure).                Multiple rules for a metadataKey can exist with different effective at dates, when resources are accessed the rule that is active for the current time will be fetched.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    LegalEntitiesApi
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
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(LegalEntitiesApi)
        id_type_scope = 'id_type_scope_example' # str | Scope of the Legal Entity identifier.
        id_type_code = 'id_type_code_example' # str | Code of the Legal Entity identifier.
        code = 'code_example' # str | Code of the Legal Entity under specified identifier type's scope and code.
        access_metadata_operation = [{"value":[{"value":"SilverLicence","provider":"TestDataProvider"}],"path":"/exampleMetadataKey","op":"add"}] # List[AccessMetadataOperation] | The Json Patch document
        effective_at = 'effective_at_example' # str | The effectiveAt datetime at which to upsert the Access Metadata (optional)
        effective_until = '2013-10-20T19:20:30+01:00' # datetime | The effective datetime until which the Access Metadata is valid. If not supplied this will be valid indefinitely, or until the next 'effectiveAt' datetime of the Access Metadata (optional)

        try:
            # [EARLY ACCESS] PatchLegalEntityAccessMetadata: Patch Access Metadata rules for a Legal Entity.
            api_response = await api_instance.patch_legal_entity_access_metadata(id_type_scope, id_type_code, code, access_metadata_operation, effective_at=effective_at, effective_until=effective_until)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling LegalEntitiesApi->patch_legal_entity_access_metadata: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_type_scope** | **str**| Scope of the Legal Entity identifier. | 
 **id_type_code** | **str**| Code of the Legal Entity identifier. | 
 **code** | **str**| Code of the Legal Entity under specified identifier type&#39;s scope and code. | 
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

# **set_legal_entity_identifiers**
> LegalEntity set_legal_entity_identifiers(id_type_scope, id_type_code, code, set_legal_entity_identifiers_request)

[EARLY ACCESS] SetLegalEntityIdentifiers: Set Legal Entity Identifiers

Set identifiers of the Legal Entity.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    LegalEntitiesApi
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
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(LegalEntitiesApi)
        id_type_scope = 'id_type_scope_example' # str | Scope of the legal entity identifier type.
        id_type_code = 'id_type_code_example' # str | Code of the legal entity identifier type.
        code = 'code_example' # str | Code of the legal entity under specified identifier type's scope and code. This together with stated identifier type uniquely              identifies the legal entity.

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # set_legal_entity_identifiers_request = SetLegalEntityIdentifiersRequest()
        # set_legal_entity_identifiers_request = SetLegalEntityIdentifiersRequest.from_json("")
        set_legal_entity_identifiers_request = SetLegalEntityIdentifiersRequest.from_dict({"identifiers":{"LegalEntity/ExternalIdentifier/LEI":{"key":"LegalEntity/ExternalIdentifier/LEI","value":{"labelValue":"LEI_12345678"}},"LegalEntity/InternalIdentifier/InternalLeiId":{"key":"LegalEntity/InternalIdentifier/InternalLeiId","value":{"labelValue":"Internal_XHSP2038"}}}}) # SetLegalEntityIdentifiersRequest | Request containing identifiers to set for the legal entity. Identifiers not specified in request will not be changed.

        try:
            # [EARLY ACCESS] SetLegalEntityIdentifiers: Set Legal Entity Identifiers
            api_response = await api_instance.set_legal_entity_identifiers(id_type_scope, id_type_code, code, set_legal_entity_identifiers_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling LegalEntitiesApi->set_legal_entity_identifiers: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_type_scope** | **str**| Scope of the legal entity identifier type. | 
 **id_type_code** | **str**| Code of the legal entity identifier type. | 
 **code** | **str**| Code of the legal entity under specified identifier type&#39;s scope and code. This together with stated identifier type uniquely              identifies the legal entity. | 
 **set_legal_entity_identifiers_request** | [**SetLegalEntityIdentifiersRequest**](SetLegalEntityIdentifiersRequest.md)| Request containing identifiers to set for the legal entity. Identifiers not specified in request will not be changed. | 

### Return type

[**LegalEntity**](LegalEntity.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Legal Entity with updated identifiers |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **set_legal_entity_properties**
> LegalEntity set_legal_entity_properties(id_type_scope, id_type_code, code, set_legal_entity_properties_request)

SetLegalEntityProperties: Set Legal Entity Properties

Set properties of the legal entity.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    LegalEntitiesApi
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
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(LegalEntitiesApi)
        id_type_scope = 'id_type_scope_example' # str | Scope of the legal entity identifier type.
        id_type_code = 'id_type_code_example' # str | Code of the legal entity identifier type.
        code = 'code_example' # str | Code of the legal entity under specified identifier type's scope and code. This together with stated identifier type uniquely              identifies the legal entity.

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # set_legal_entity_properties_request = SetLegalEntityPropertiesRequest()
        # set_legal_entity_properties_request = SetLegalEntityPropertiesRequest.from_json("")
        set_legal_entity_properties_request = SetLegalEntityPropertiesRequest.from_dict({"properties":{"LegalEntity/Details/Name":{"key":"LegalEntity/Details/Name","value":{"labelValue":"John Smith"},"effectiveFrom":"2016-07-01T00:00:00.0000000+00:00"},"LegalEntity/Details/Country":{"key":"LegalEntity/Details/Country","value":{"labelValue":"United Kingdom"},"effectiveFrom":"2016-07-01T00:00:00.0000000+00:00"}}}) # SetLegalEntityPropertiesRequest | Request containing properties to set for the legal entity. Properties not specified in request will not be changed.

        try:
            # SetLegalEntityProperties: Set Legal Entity Properties
            api_response = await api_instance.set_legal_entity_properties(id_type_scope, id_type_code, code, set_legal_entity_properties_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling LegalEntitiesApi->set_legal_entity_properties: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_type_scope** | **str**| Scope of the legal entity identifier type. | 
 **id_type_code** | **str**| Code of the legal entity identifier type. | 
 **code** | **str**| Code of the legal entity under specified identifier type&#39;s scope and code. This together with stated identifier type uniquely              identifies the legal entity. | 
 **set_legal_entity_properties_request** | [**SetLegalEntityPropertiesRequest**](SetLegalEntityPropertiesRequest.md)| Request containing properties to set for the legal entity. Properties not specified in request will not be changed. | 

### Return type

[**LegalEntity**](LegalEntity.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Legal Entity with updated properties |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **upsert_legal_entities**
> UpsertLegalEntitiesResponse upsert_legal_entities(success_mode, request_body)

[EARLY ACCESS] UpsertLegalEntities: Pluralised upsert of Legal Entities

Creates or updates a collection of Legal Entities

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    LegalEntitiesApi
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
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(LegalEntitiesApi)
        success_mode = 'success_mode_example' # str | Whether the batch request should fail Atomically or in a Partial fashion - Allowed Values: Atomic, Partial
        request_body = {"firstExampleRequest":{"identifiers":{"LegalEntity/ExternalIdentifier/LEI":{"key":"LegalEntity/ExternalIdentifier/LEI","value":{"labelValue":"LEI_12345678"}},"LegalEntity/InternalIdentifier/InternalLeiId":{"key":"LegalEntity/InternalIdentifier/InternalLeiId","value":{"labelValue":"Internal_XHSP2038"}}},"properties":{"LegalEntity/Details/Name":{"key":"LegalEntity/Details/Name","value":{"labelValue":"Legal Entity Inc."}},"LegalEntity/Details/Country":{"key":"LegalEntity/Details/Country","value":{"labelValue":"United Kingdom"},"effectiveFrom":"2016-01-01T00:00:00.0000000+00:00"},"LegalEntity/Status/Active":{"key":"LegalEntity/Status/Active","value":{"labelValue":"Active"},"effectiveFrom":"2016-07-01T00:00:00.0000000+00:00"}},"displayName":"LegalEntity1DisplayName","description":"LegalEntity1Description","counterpartyRiskInformation":{"countryOfRisk":"UnitedKingdom","creditRatings":[{"ratingSource":"StandardAndPoors","rating":"AA+"}],"industryClassifiers":[{"classificationSystemName":"GICS2018","classificationCode":"10101010"}]}},"secondExampleRequest":{"identifiers":{"LegalEntity/ExternalIdentifier/LEI":{"key":"LegalEntity/ExternalIdentifier/LEI","value":{"labelValue":"LEI_22345678"}},"LegalEntity/InternalIdentifier/InternalLeiId":{"key":"LegalEntity/InternalIdentifier/InternalLeiId","value":{"labelValue":"Internal_XHSP2038"}}},"properties":{"LegalEntity/Details/Name":{"key":"LegalEntity/Details/Name","value":{"labelValue":"Legal Entity 2 Inc."}},"LegalEntity/Details/Country":{"key":"LegalEntity/Details/Country","value":{"labelValue":"Germany"},"effectiveFrom":"2016-01-01T00:00:00.0000000+00:00"},"LegalEntity/Status/Active":{"key":"LegalEntity/Status/Active","value":{"labelValue":"Active"},"effectiveFrom":"2016-04-01T00:00:00.0000000+00:00"}},"displayName":"LegalEntity2DisplayName","description":"LegalEntity2Description"}} # Dict[str, UpsertLegalEntityRequest] | A collection of requests to create or update Legal Entities.

        try:
            # [EARLY ACCESS] UpsertLegalEntities: Pluralised upsert of Legal Entities
            api_response = await api_instance.upsert_legal_entities(success_mode, request_body)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling LegalEntitiesApi->upsert_legal_entities: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **success_mode** | **str**| Whether the batch request should fail Atomically or in a Partial fashion - Allowed Values: Atomic, Partial | 
 **request_body** | [**Dict[str, UpsertLegalEntityRequest]**](UpsertLegalEntityRequest.md)| A collection of requests to create or update Legal Entities. | 

### Return type

[**UpsertLegalEntitiesResponse**](UpsertLegalEntitiesResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The successfully created or updated legal entities along with any failures |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **upsert_legal_entity**
> LegalEntity upsert_legal_entity(upsert_legal_entity_request)

UpsertLegalEntity: Upsert Legal Entity

Create or update a legal entity

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    LegalEntitiesApi
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
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(LegalEntitiesApi)

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # upsert_legal_entity_request = UpsertLegalEntityRequest()
        # upsert_legal_entity_request = UpsertLegalEntityRequest.from_json("")
        upsert_legal_entity_request = UpsertLegalEntityRequest.from_dict({"identifiers":{"LegalEntity/ExternalIdentifier/LEI":{"key":"LegalEntity/ExternalIdentifier/LEI","value":{"labelValue":"LEI_12345678"}},"LegalEntity/InternalIdentifier/InternalLeiId":{"key":"LegalEntity/InternalIdentifier/InternalLeiId","value":{"labelValue":"Internal_XHSP2038"}}},"properties":{"LegalEntity/Details/Name":{"key":"LegalEntity/Details/Name","value":{"labelValue":"Legal Entity Inc."}},"LegalEntity/Details/Country":{"key":"LegalEntity/Details/Country","value":{"labelValue":"United Kingdom"},"effectiveFrom":"2016-01-01T00:00:00.0000000+00:00"},"LegalEntity/Status/Active":{"key":"LegalEntity/Status/Active","value":{"labelValue":"Active"},"effectiveFrom":"2016-07-01T00:00:00.0000000+00:00"}},"displayName":"LegalEntity1DisplayName","description":"LegalEntity1Description","counterpartyRiskInformation":{"countryOfRisk":"UnitedKingdom","creditRatings":[{"ratingSource":"StandardAndPoors","rating":"AA+"}],"industryClassifiers":[{"classificationSystemName":"GICS2018","classificationCode":"10101010"}]}}) # UpsertLegalEntityRequest | Request to create or update a legal entity.

        try:
            # UpsertLegalEntity: Upsert Legal Entity
            api_response = await api_instance.upsert_legal_entity(upsert_legal_entity_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling LegalEntitiesApi->upsert_legal_entity: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_legal_entity_request** | [**UpsertLegalEntityRequest**](UpsertLegalEntityRequest.md)| Request to create or update a legal entity. | 

### Return type

[**LegalEntity**](LegalEntity.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created or updated legal entity |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **upsert_legal_entity_access_metadata**
> ResourceListOfAccessMetadataValueOf upsert_legal_entity_access_metadata(id_type_scope, id_type_code, code, metadata_key, upsert_legal_entity_access_metadata_request, effective_at=effective_at, effective_until=effective_until)

[EARLY ACCESS] UpsertLegalEntityAccessMetadata: Upsert a Legal Entity Access Metadata entry associated with a specific metadataKey. This creates or updates the data in LUSID.

Update or insert one Legal Entity Access Metadata entry in a single scope. An item will be updated if it already exists  and inserted if it does not.                The response will return the successfully updated or inserted Legal Entity Access Metadata rule or failure message if unsuccessful.                It is important to always check to verify success (or failure).                Multiple rules for a metadataKey can exist with different effective at dates, when resources are accessed the rule that is active for the current time will be fetched.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    LegalEntitiesApi
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
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(LegalEntitiesApi)
        id_type_scope = 'id_type_scope_example' # str | Scope of the Legal Entity identifier.
        id_type_code = 'id_type_code_example' # str | Code of the Legal Entity identifier.
        code = 'code_example' # str | Code of the Legal Entity under specified identifier type's scope and code.
        metadata_key = 'metadata_key_example' # str | Key of the metadata entry to retrieve

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # upsert_legal_entity_access_metadata_request = UpsertLegalEntityAccessMetadataRequest()
        # upsert_legal_entity_access_metadata_request = UpsertLegalEntityAccessMetadataRequest.from_json("")
        upsert_legal_entity_access_metadata_request = UpsertLegalEntityAccessMetadataRequest.from_dict({"metadata":[{"value":"SilverLicence","provider":"TestDataProvider"}]}) # UpsertLegalEntityAccessMetadataRequest | The Legal Entity Access Metadata entry to upsert
        effective_at = 'effective_at_example' # str | The effectiveAt datetime at which to upsert the Access Metadata (optional)
        effective_until = '2013-10-20T19:20:30+01:00' # datetime | The effective datetime until which the Access Metadata is valid. If not supplied this will be valid indefinitely, or until the next 'effectiveAt' datetime of the Access Metadata (optional)

        try:
            # [EARLY ACCESS] UpsertLegalEntityAccessMetadata: Upsert a Legal Entity Access Metadata entry associated with a specific metadataKey. This creates or updates the data in LUSID.
            api_response = await api_instance.upsert_legal_entity_access_metadata(id_type_scope, id_type_code, code, metadata_key, upsert_legal_entity_access_metadata_request, effective_at=effective_at, effective_until=effective_until)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling LegalEntitiesApi->upsert_legal_entity_access_metadata: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_type_scope** | **str**| Scope of the Legal Entity identifier. | 
 **id_type_code** | **str**| Code of the Legal Entity identifier. | 
 **code** | **str**| Code of the Legal Entity under specified identifier type&#39;s scope and code. | 
 **metadata_key** | **str**| Key of the metadata entry to retrieve | 
 **upsert_legal_entity_access_metadata_request** | [**UpsertLegalEntityAccessMetadataRequest**](UpsertLegalEntityAccessMetadataRequest.md)| The Legal Entity Access Metadata entry to upsert | 
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

