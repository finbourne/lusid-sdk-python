# lusid.ScriptedTranslationApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_translation_dialect**](ScriptedTranslationApi.md#get_translation_dialect) | **GET** /api/scriptedtranslation/dialects/{scope}/{vendor}/{sourceSystem}/{entityType}/{serialisationFormat}/{version} | [EARLY ACCESS] GetTranslationDialect: Get a dialect.
[**get_translation_script**](ScriptedTranslationApi.md#get_translation_script) | **GET** /api/scriptedtranslation/scripts/{scope}/{code}/{version} | [EARLY ACCESS] GetTranslationScript: Retrieve a translation script by its identifier.
[**list_dialect_ids**](ScriptedTranslationApi.md#list_dialect_ids) | **GET** /api/scriptedtranslation/dialects/ids | [EARLY ACCESS] ListDialectIds: List dialect identifiers matching an optional filter.
[**list_translation_script_ids**](ScriptedTranslationApi.md#list_translation_script_ids) | **GET** /api/scriptedtranslation/scripts/ids | [EARLY ACCESS] ListTranslationScriptIds: List translation script identifiers.
[**translate_entities**](ScriptedTranslationApi.md#translate_entities) | **POST** /api/scriptedtranslation/translateentities | [EARLY ACCESS] TranslateEntities: Translate a collection of entities with a specified translation script.
[**translate_entities_inlined**](ScriptedTranslationApi.md#translate_entities_inlined) | **POST** /api/scriptedtranslation/translateentitiesinlined | [EARLY ACCESS] TranslateEntitiesInlined: Translate a collection of entities, inlining the body of the translation script.
[**upsert_translation_dialect**](ScriptedTranslationApi.md#upsert_translation_dialect) | **POST** /api/scriptedtranslation/dialects | [EARLY ACCESS] UpsertTranslationDialect: Upsert a Dialect.
[**upsert_translation_script**](ScriptedTranslationApi.md#upsert_translation_script) | **POST** /api/scriptedtranslation/scripts | [EARLY ACCESS] UpsertTranslationScript: Upsert a translation script.


# **get_translation_dialect**
> Dialect get_translation_dialect(scope, vendor, source_system, entity_type, serialisation_format, version, as_at=as_at)

[EARLY ACCESS] GetTranslationDialect: Get a dialect.

Get the dialect with the given identifier at the specific asAt time.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    ScriptedTranslationApi
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
        api_instance = api_client_factory.build(ScriptedTranslationApi)
        scope = 'scope_example' # str | The scope of the dialect.
        vendor = 'vendor_example' # str | The vendor of the dialect, the entity that created it. e.g. ISDA, FINBOURNE.
        source_system = 'source_system_example' # str | The source system of the dialect, the system that understands it. e.g. LUSID, QuantLib.
        entity_type = 'entity_type_example' # str | The type of entity this dialect describes e.g. Instrument.
        serialisation_format = 'serialisation_format_example' # str | The serialisation format of a document in this dialect. e.g. JSON, XML.
        version = 'version_example' # str | The semantic version of the dialect: MAJOR.MINOR.PATCH.
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the dialect. Defaults to return the latest version of the dialect if not specified. (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.get_translation_dialect(scope, vendor, source_system, entity_type, serialisation_format, version, as_at=as_at, opts=opts)

            # [EARLY ACCESS] GetTranslationDialect: Get a dialect.
            api_response = await api_instance.get_translation_dialect(scope, vendor, source_system, entity_type, serialisation_format, version, as_at=as_at)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ScriptedTranslationApi->get_translation_dialect: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the dialect. | 
 **vendor** | **str**| The vendor of the dialect, the entity that created it. e.g. ISDA, FINBOURNE. | 
 **source_system** | **str**| The source system of the dialect, the system that understands it. e.g. LUSID, QuantLib. | 
 **entity_type** | **str**| The type of entity this dialect describes e.g. Instrument. | 
 **serialisation_format** | **str**| The serialisation format of a document in this dialect. e.g. JSON, XML. | 
 **version** | **str**| The semantic version of the dialect: MAJOR.MINOR.PATCH. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the dialect. Defaults to return the latest version of the dialect if not specified. | [optional] 

### Return type

[**Dialect**](Dialect.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The dialect with the given ID. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_translation_script**
> TranslationScript get_translation_script(scope, code, version, as_at=as_at)

[EARLY ACCESS] GetTranslationScript: Retrieve a translation script by its identifier.

Retrieves a translation script to be used for translating financial entities.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    ScriptedTranslationApi
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
        api_instance = api_client_factory.build(ScriptedTranslationApi)
        scope = 'scope_example' # str | Scope of the translation script.
        code = 'code_example' # str | Code of the translation script.
        version = 'version_example' # str | Semantic version of the translation script.
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the translation script. Defaults to latest. (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.get_translation_script(scope, code, version, as_at=as_at, opts=opts)

            # [EARLY ACCESS] GetTranslationScript: Retrieve a translation script by its identifier.
            api_response = await api_instance.get_translation_script(scope, code, version, as_at=as_at)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ScriptedTranslationApi->get_translation_script: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of the translation script. | 
 **code** | **str**| Code of the translation script. | 
 **version** | **str**| Semantic version of the translation script. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the translation script. Defaults to latest. | [optional] 

### Return type

[**TranslationScript**](TranslationScript.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested translation script. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_dialect_ids**
> PagedResourceListOfDialectId list_dialect_ids(as_at=as_at, page=page, limit=limit, filter=filter)

[EARLY ACCESS] ListDialectIds: List dialect identifiers matching an optional filter.

List the stored dialects' identifiers with pagination and filtering at the specified asAt time.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    ScriptedTranslationApi
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
        api_instance = api_client_factory.build(ScriptedTranslationApi)
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the dialects.              Defaults to return the latest version of the dialect if not specified. (optional)
        page = 'page_example' # str | The pagination token to use to continue listing dialect IDs from a previous call to list dialect IDs.              This value is returned from the previous call. If a pagination token is provided the filter and asAt fields              must not have changed since the original request. (optional)
        limit = 56 # int | When paginating, limit the number of returned results to this many. (optional)
        filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.list_dialect_ids(as_at=as_at, page=page, limit=limit, filter=filter, opts=opts)

            # [EARLY ACCESS] ListDialectIds: List dialect identifiers matching an optional filter.
            api_response = await api_instance.list_dialect_ids(as_at=as_at, page=page, limit=limit, filter=filter)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ScriptedTranslationApi->list_dialect_ids: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to retrieve the dialects.              Defaults to return the latest version of the dialect if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing dialect IDs from a previous call to list dialect IDs.              This value is returned from the previous call. If a pagination token is provided the filter and asAt fields              must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**PagedResourceListOfDialectId**](PagedResourceListOfDialectId.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of dialect IDs. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_translation_script_ids**
> PagedResourceListOfTranslationScriptId list_translation_script_ids(as_at=as_at, limit=limit, filter=filter, page=page)

[EARLY ACCESS] ListTranslationScriptIds: List translation script identifiers.

List translation script ids.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    ScriptedTranslationApi
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
        api_instance = api_client_factory.build(ScriptedTranslationApi)
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the script identifiers. Defaults to latest. (optional)
        limit = 56 # int | When paginating, limit the results to this number. Defaults to 100 if not specified. (optional)
        filter = 'filter_example' # str | Expression to filter the results. For example, Id.Version.Major eq 1 to list IDs with major version 1              or Id.Scope eq 'my-scripts' to list result only for a particular scope. (optional)
        page = 'page_example' # str | The pagination token to use to continue listing translation script IDs; this              value is returned from the previous call. If a pagination token is provided, the filter field              must not have changed since the original request. (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.list_translation_script_ids(as_at=as_at, limit=limit, filter=filter, page=page, opts=opts)

            # [EARLY ACCESS] ListTranslationScriptIds: List translation script identifiers.
            api_response = await api_instance.list_translation_script_ids(as_at=as_at, limit=limit, filter=filter, page=page)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ScriptedTranslationApi->list_translation_script_ids: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to retrieve the script identifiers. Defaults to latest. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results. For example, Id.Version.Major eq 1 to list IDs with major version 1              or Id.Scope eq &#39;my-scripts&#39; to list result only for a particular scope. | [optional] 
 **page** | **str**| The pagination token to use to continue listing translation script IDs; this              value is returned from the previous call. If a pagination token is provided, the filter field              must not have changed since the original request. | [optional] 

### Return type

[**PagedResourceListOfTranslationScriptId**](PagedResourceListOfTranslationScriptId.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested translation script IDs. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **translate_entities**
> TranslateEntitiesResponse translate_entities(translate_entities_request)

[EARLY ACCESS] TranslateEntities: Translate a collection of entities with a specified translation script.

Run the provided translation request. The entities to translate are specified in the request body as a  dictionary with (ephemeral) unique correlation IDs. The script to use and optional dialect to validate  results against are sourced from the database.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    ScriptedTranslationApi
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
        api_instance = api_client_factory.build(ScriptedTranslationApi)

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # translate_entities_request = TranslateEntitiesRequest()
        # translate_entities_request = TranslateEntitiesRequest.from_json("")
        translate_entities_request = TranslateEntitiesRequest.from_dict({"entityPayloads":{"myFxFwd-0":{"entity":"{ \"startDate\": \"2018-01-01T00:00:00.0000000+00:00\", \"maturityDate\": \"2019-01-01T00:00:00.0000000+00:00\", \"domAmount\": 1, \"domCcy\": \"GBP\", \"fgnAmount\": -1.5,  \"fgnCcy\": \"USD\",  \"refSpotRate\": 1.5,  \"isNdf\": false, \"fixingDate\": \"0001-01-01T00:00:00.0000000+00:00\",  \"instrumentType\": \"FxForward\" }"}},"scriptId":{"scope":"example-scope","code":"example-code","version":"0.0.1"},"dialectId":{"scope":"scope-A","vendor":"BigBankCorporation","sourceSystem":"InstrumentMaster","version":"2.1.4","serialisationFormat":"Json","entityType":"Instrument"}}) # TranslateEntitiesRequest | The entities to translate, along with identifiers for the script and (optional) dialect to use.

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.translate_entities(translate_entities_request, opts=opts)

            # [EARLY ACCESS] TranslateEntities: Translate a collection of entities with a specified translation script.
            api_response = await api_instance.translate_entities(translate_entities_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ScriptedTranslationApi->translate_entities: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **translate_entities_request** | [**TranslateEntitiesRequest**](TranslateEntitiesRequest.md)| The entities to translate, along with identifiers for the script and (optional) dialect to use. | 

### Return type

[**TranslateEntitiesResponse**](TranslateEntitiesResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The translated entities along with any errors for entities that failed to be translated indexed by their correlation IDs. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **translate_entities_inlined**
> TranslateEntitiesResponse translate_entities_inlined(translate_entities_inlined_request)

[EARLY ACCESS] TranslateEntitiesInlined: Translate a collection of entities, inlining the body of the translation script.

Run the provided translation request. The entities to translate, script to use and dialect to validate results against  are all specified in the request body. The entities are given as a dictionary with (ephemeral) unique correlation IDs.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    ScriptedTranslationApi
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
        api_instance = api_client_factory.build(ScriptedTranslationApi)

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # translate_entities_inlined_request = TranslateEntitiesInlinedRequest()
        # translate_entities_inlined_request = TranslateEntitiesInlinedRequest.from_json("")
        translate_entities_inlined_request = TranslateEntitiesInlinedRequest.from_dict({"entityPayloads":{"myFxFwd-0":{"entity":"{\r\n \"startDate\": \"2018-01-01T00:00:00.0000000+00:00\",\r\n \"maturityDate\": \"2019-01-01T00:00:00.0000000+00:00\",\r\n \"domAmount\": 1,\r\n \"domCcy\": \"GBP\",\r\n \"fgnAmount\": -1.5,\r\n  \"fgnCcy\": \"USD\",\r\n      \"refSpotRate\": 1.5,\r\n \"isNdf\": false,\r\n \"fixingDate\": \"0001-01-01T00:00:00.0000000+00:00\",\r\n \"instrumentType\": \"FxForward\"\r\n}"},"myFxFwd-that-will-fail-translation":{"entity":"some-bad-payload"}},"scriptBody":"export function entryPoint() { return { scriptInterfaceVersion: 1, translate: Translate }; } function Translate(input){ const fxfwd = JSON.parse(input);  fxfwd[\"endDate\"] = fxfwd[\"maturityDate\"];  delete fxfwd[\"maturityDate\"];  return JSON.stringify(fxfwd); }","schema":{"type":"JsonSchema","body":"{\n  \"type\": \"object\",\n  \"properties\": {\n    \"Identifier\": {\n      \"type\": \"string\",\n      \"pattern\": \"/^[a-f\\\\d]{4}(?:[a-f\\\\d]{4}-){4}[a-f\\\\d]{12}$/i\"\n    },\n    \"AssetClass\": {\n      \"type\": \"string\",\n      \"enum\": [\n        \"Rates\",\n        \"Fx\",\n        \"Equity\",\n        \"Credit\"\n      ]\n    },\n    \"StartDate\": {\n      \"type\": \"string\",\n      \"format\": \"date-time\"\n    },\n    \"MaturityDate\": {\n      \"type\": \"string\",\n      \"format\": \"date-time\"\n    },\n    \"Notional\": {\n      \"type\": \"number\"\n    }\n  },\n  \"required\": [\n    \"Identifier\",\n    \"AssetClass\",\n    \"StartDate\",\n    \"MaturityDate\",\n    \"Notional\"\n  ]\n}"}}) # TranslateEntitiesInlinedRequest | The entities to translate, along with the script to use and an optional schema for validation.

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.translate_entities_inlined(translate_entities_inlined_request, opts=opts)

            # [EARLY ACCESS] TranslateEntitiesInlined: Translate a collection of entities, inlining the body of the translation script.
            api_response = await api_instance.translate_entities_inlined(translate_entities_inlined_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ScriptedTranslationApi->translate_entities_inlined: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **translate_entities_inlined_request** | [**TranslateEntitiesInlinedRequest**](TranslateEntitiesInlinedRequest.md)| The entities to translate, along with the script to use and an optional schema for validation. | 

### Return type

[**TranslateEntitiesResponse**](TranslateEntitiesResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The translated entities along with any errors for entities that failed to be translated indexed by their correlation IDs. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **upsert_translation_dialect**
> Dialect upsert_translation_dialect(upsert_dialect_request)

[EARLY ACCESS] UpsertTranslationDialect: Upsert a Dialect.

Upsert the given dialect.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    ScriptedTranslationApi
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
        api_instance = api_client_factory.build(ScriptedTranslationApi)

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # upsert_dialect_request = UpsertDialectRequest()
        # upsert_dialect_request = UpsertDialectRequest.from_json("")
        upsert_dialect_request = UpsertDialectRequest.from_dict({"id":{"scope":"scope-A","vendor":"BigBankCorporation","sourceSystem":"InstrumentMaster","version":"2.1.4","serialisationFormat":"Json","entityType":"Instrument"},"schema":{"type":"JsonSchema","body":"{\n  \"type\": \"object\",\n  \"properties\": {\n    \"Identifier\": {\n      \"type\": \"string\",\n      \"pattern\": \"/^[a-f\\\\d]{4}(?:[a-f\\\\d]{4}-){4}[a-f\\\\d]{12}$/i\"\n    },\n    \"AssetClass\": {\n      \"type\": \"string\",\n      \"enum\": [\n        \"Rates\",\n        \"Fx\",\n        \"Equity\",\n        \"Credit\"\n      ]\n    },\n    \"StartDate\": {\n      \"type\": \"string\",\n      \"format\": \"date-time\"\n    },\n    \"MaturityDate\": {\n      \"type\": \"string\",\n      \"format\": \"date-time\"\n    },\n    \"Notional\": {\n      \"type\": \"number\"\n    }\n  },\n  \"required\": [\n    \"Identifier\",\n    \"AssetClass\",\n    \"StartDate\",\n    \"MaturityDate\",\n    \"Notional\"\n  ]\n}"}}) # UpsertDialectRequest | The dialect to upsert.

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.upsert_translation_dialect(upsert_dialect_request, opts=opts)

            # [EARLY ACCESS] UpsertTranslationDialect: Upsert a Dialect.
            api_response = await api_instance.upsert_translation_dialect(upsert_dialect_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ScriptedTranslationApi->upsert_translation_dialect: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_dialect_request** | [**UpsertDialectRequest**](UpsertDialectRequest.md)| The dialect to upsert. | 

### Return type

[**Dialect**](Dialect.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The upserted dialect. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **upsert_translation_script**
> TranslationScript upsert_translation_script(upsert_translation_script_request)

[EARLY ACCESS] UpsertTranslationScript: Upsert a translation script.

Upserts a translation script to be used for translating financial entities.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    ScriptedTranslationApi
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
        api_instance = api_client_factory.build(ScriptedTranslationApi)

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # upsert_translation_script_request = UpsertTranslationScriptRequest()
        # upsert_translation_script_request = UpsertTranslationScriptRequest.from_json("")
        upsert_translation_script_request = UpsertTranslationScriptRequest.from_dict({"id":{"scope":"example-scope","code":"example-code","version":"0.0.1"},"body":"export function entryPoint() { return { scriptInterfaceVersion: 1, translate: Translate }; } function Translate(input){ const fxfwd = JSON.parse(input);  fxfwd[\"endDate\"] = fxfwd[\"maturityDate\"];  delete fxfwd[\"maturityDate\"];  return JSON.stringify(fxfwd); }"}) # UpsertTranslationScriptRequest | The translation script to be upserted.

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.upsert_translation_script(upsert_translation_script_request, opts=opts)

            # [EARLY ACCESS] UpsertTranslationScript: Upsert a translation script.
            api_response = await api_instance.upsert_translation_script(upsert_translation_script_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ScriptedTranslationApi->upsert_translation_script: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_translation_script_request** | [**UpsertTranslationScriptRequest**](UpsertTranslationScriptRequest.md)| The translation script to be upserted. | 

### Return type

[**TranslationScript**](TranslationScript.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully created translation script. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

