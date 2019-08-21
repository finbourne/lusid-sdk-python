# lusid.InstrumentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_instrument**](InstrumentsApi.md#delete_instrument) | **DELETE** /api/instruments/{identifierType}/{identifier} | [EARLY ACCESS] Delete instrument
[**get_instrument**](InstrumentsApi.md#get_instrument) | **GET** /api/instruments/{identifierType}/{identifier} | [EARLY ACCESS] Get instrument
[**get_instrument_identifier_types**](InstrumentsApi.md#get_instrument_identifier_types) | **GET** /api/instruments/identifierTypes | [EARLY ACCESS] Get instrument identifier types
[**get_instruments**](InstrumentsApi.md#get_instruments) | **POST** /api/instruments/$get | [EARLY ACCESS] Get instruments
[**list_instruments**](InstrumentsApi.md#list_instruments) | **GET** /api/instruments | [EARLY ACCESS] List instruments
[**update_instrument_identifier**](InstrumentsApi.md#update_instrument_identifier) | **POST** /api/instruments/{identifierType}/{identifier} | [EARLY ACCESS] Update instrument identifier
[**upsert_instruments**](InstrumentsApi.md#upsert_instruments) | **POST** /api/instruments | [EARLY ACCESS] Upsert instruments
[**upsert_instruments_properties**](InstrumentsApi.md#upsert_instruments_properties) | **POST** /api/instruments/$upsertproperties | [EARLY ACCESS] Upsert instruments properties


# **delete_instrument**
> DeleteInstrumentResponse delete_instrument(identifier_type, identifier)

[EARLY ACCESS] Delete instrument

Delete a single instrument identified by a unique instrument identifier. Once an instrument has been  deleted it will be marked as 'inactive' and it can no longer be used when updating or inserting transactions or holdings.  You can still query existing transactions and holdings related to the deleted instrument.

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

# create an instance of the API class
api_instance = lusid.InstrumentsApi(lusid.ApiClient(configuration))
identifier_type = 'identifier_type_example' # str | The identifier being supplied e.g. \"Figi\".
identifier = 'identifier_example' # str | The value of the identifier that resolves to the instrument to delete.

try:
    # [EARLY ACCESS] Delete instrument
    api_response = api_instance.delete_instrument(identifier_type, identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstrumentsApi->delete_instrument: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier_type** | **str**| The identifier being supplied e.g. \&quot;Figi\&quot;. | 
 **identifier** | **str**| The value of the identifier that resolves to the instrument to delete. | 

### Return type

[**DeleteInstrumentResponse**](DeleteInstrumentResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_instrument**
> Instrument get_instrument(identifier_type, identifier, effective_at=effective_at, as_at=as_at, instrument_property_keys=instrument_property_keys)

[EARLY ACCESS] Get instrument

Get the definition of a single instrument identified by a unique instrument identifier.

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

# create an instance of the API class
api_instance = lusid.InstrumentsApi(lusid.ApiClient(configuration))
identifier_type = 'identifier_type_example' # str | The identifier being supplied e.g. \"Figi\".
identifier = 'identifier_example' # str | The value of the identifier for the requested instrument.
effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the instrument definition.              Defaults to the current LUSID system datetime if not specified. (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the instrument definition. Defaults to              return the latest version of the instrument definition if not specified. (optional)
instrument_property_keys = ['instrument_property_keys_example'] # list[str] | A list of property keys from the \"Instrument\" domain to decorate onto the instrument.              These take the format {domain}/{scope}/{code} e.g. \"Instrument/system/Name\". (optional)

try:
    # [EARLY ACCESS] Get instrument
    api_response = api_instance.get_instrument(identifier_type, identifier, effective_at=effective_at, as_at=as_at, instrument_property_keys=instrument_property_keys)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstrumentsApi->get_instrument: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier_type** | **str**| The identifier being supplied e.g. \&quot;Figi\&quot;. | 
 **identifier** | **str**| The value of the identifier for the requested instrument. | 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the instrument definition.              Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the instrument definition. Defaults to              return the latest version of the instrument definition if not specified. | [optional] 
 **instrument_property_keys** | [**list[str]**](str.md)| A list of property keys from the \&quot;Instrument\&quot; domain to decorate onto the instrument.              These take the format {domain}/{scope}/{code} e.g. \&quot;Instrument/system/Name\&quot;. | [optional] 

### Return type

[**Instrument**](Instrument.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_instrument_identifier_types**
> ResourceListOfInstrumentIdTypeDescriptor get_instrument_identifier_types()

[EARLY ACCESS] Get instrument identifier types

Get the allowable instrument identifier types and their descriptions.

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

# create an instance of the API class
api_instance = lusid.InstrumentsApi(lusid.ApiClient(configuration))

try:
    # [EARLY ACCESS] Get instrument identifier types
    api_response = api_instance.get_instrument_identifier_types()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstrumentsApi->get_instrument_identifier_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResourceListOfInstrumentIdTypeDescriptor**](ResourceListOfInstrumentIdTypeDescriptor.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_instruments**
> GetInstrumentsResponse get_instruments(identifier_type, identifiers, effective_at=effective_at, as_at=as_at, instrument_property_keys=instrument_property_keys)

[EARLY ACCESS] Get instruments

Get the definition of one or more instruments identified by a collection of unique instrument identifiers.

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

# create an instance of the API class
api_instance = lusid.InstrumentsApi(lusid.ApiClient(configuration))
identifier_type = 'identifier_type_example' # str | The identifier being supplied e.g. \"Figi\".
identifiers = None # list[str] | The values of the identifier for the requested instruments.
effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the instrument definitions.              Defaults to the current LUSID system datetime if not specified. (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the instrument definitions.              Defaults to return the latest version of each instrument definition if not specified. (optional)
instrument_property_keys = ['instrument_property_keys_example'] # list[str] | A list of property keys from the \"Instrument\" domain to decorate onto the instrument.              These take the format {domain}/{scope}/{code} e.g. \"Instrument/system/Name\". (optional)

try:
    # [EARLY ACCESS] Get instruments
    api_response = api_instance.get_instruments(identifier_type, identifiers, effective_at=effective_at, as_at=as_at, instrument_property_keys=instrument_property_keys)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstrumentsApi->get_instruments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier_type** | **str**| The identifier being supplied e.g. \&quot;Figi\&quot;. | 
 **identifiers** | [**list[str]**](list.md)| The values of the identifier for the requested instruments. | 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the instrument definitions.              Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the instrument definitions.              Defaults to return the latest version of each instrument definition if not specified. | [optional] 
 **instrument_property_keys** | [**list[str]**](str.md)| A list of property keys from the \&quot;Instrument\&quot; domain to decorate onto the instrument.              These take the format {domain}/{scope}/{code} e.g. \&quot;Instrument/system/Name\&quot;. | [optional] 

### Return type

[**GetInstrumentsResponse**](GetInstrumentsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_instruments**
> ResourceListOfInstrument list_instruments(as_at=as_at, effective_at=effective_at, page=page, sort_by=sort_by, start=start, limit=limit, filter=filter, instrument_property_keys=instrument_property_keys)

[EARLY ACCESS] List instruments

List all the instruments that have been mastered in the LUSID instrument master.  The maximum number of instruments that this method can list per request is 2,000.

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

# create an instance of the API class
api_instance = lusid.InstrumentsApi(lusid.ApiClient(configuration))
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the instruments. Defaults to return the latest              version of each instruments if not specified. (optional)
effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to list the instruments.              Defaults to the current LUSID system datetime if not specified. (optional)
page = 'page_example' # str | The pagination token to use to continue listing instruments from a previous call to list instruments.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields              must not have changed since the original request. Also, if set, a start value cannot be provided. (optional)
sort_by = ['sort_by_example'] # list[str] | Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName. (optional)
start = 56 # int | When paginating, skip this number of results. (optional)
limit = 56 # int | When paginating, limit the number of returned results to this many. (optional)
filter = 'State eq 'Active'' # str | Expression to filter the result set. Defaults to filter down to active instruments only, i.e. those              that have not been deleted. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional) (default to 'State eq 'Active'')
instrument_property_keys = ['instrument_property_keys_example'] # list[str] | A list of property keys from the \"Instrument\" domain to decorate onto each instrument. These take the format {domain}/{scope}/{code} e.g. \"Instrument/system/Name\". (optional)

try:
    # [EARLY ACCESS] List instruments
    api_response = api_instance.list_instruments(as_at=as_at, effective_at=effective_at, page=page, sort_by=sort_by, start=start, limit=limit, filter=filter, instrument_property_keys=instrument_property_keys)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstrumentsApi->list_instruments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the instruments. Defaults to return the latest              version of each instruments if not specified. | [optional] 
 **effective_at** | **str**| The effective datetime or cut label at which to list the instruments.              Defaults to the current LUSID system datetime if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing instruments from a previous call to list instruments.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields              must not have changed since the original request. Also, if set, a start value cannot be provided. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName. | [optional] 
 **start** | **int**| When paginating, skip this number of results. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Expression to filter the result set. Defaults to filter down to active instruments only, i.e. those              that have not been deleted. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] [default to &#39;State eq &#39;Active&#39;&#39;]
 **instrument_property_keys** | [**list[str]**](str.md)| A list of property keys from the \&quot;Instrument\&quot; domain to decorate onto each instrument. These take the format {domain}/{scope}/{code} e.g. \&quot;Instrument/system/Name\&quot;. | [optional] 

### Return type

[**ResourceListOfInstrument**](ResourceListOfInstrument.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_instrument_identifier**
> Instrument update_instrument_identifier(identifier_type, identifier, request)

[EARLY ACCESS] Update instrument identifier

Update, insert or delete a single instrument identifier for a single instrument. If it is not being deleted  the identifier will be updated if it already exists and inserted if it does not.

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

# create an instance of the API class
api_instance = lusid.InstrumentsApi(lusid.ApiClient(configuration))
identifier_type = 'identifier_type_example' # str | The identifier to use to resolve the instrument e.g. \"Figi\".
identifier = 'identifier_example' # str | The original value of the identifier for the requested instrument.
request = lusid.UpdateInstrumentIdentifierRequest() # UpdateInstrumentIdentifierRequest | The identifier to update or remove. This may or may not be the same identifier used              to resolve the instrument.

try:
    # [EARLY ACCESS] Update instrument identifier
    api_response = api_instance.update_instrument_identifier(identifier_type, identifier, request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstrumentsApi->update_instrument_identifier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier_type** | **str**| The identifier to use to resolve the instrument e.g. \&quot;Figi\&quot;. | 
 **identifier** | **str**| The original value of the identifier for the requested instrument. | 
 **request** | [**UpdateInstrumentIdentifierRequest**](UpdateInstrumentIdentifierRequest.md)| The identifier to update or remove. This may or may not be the same identifier used              to resolve the instrument. | 

### Return type

[**Instrument**](Instrument.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_instruments**
> UpsertInstrumentsResponse upsert_instruments(requests=requests)

[EARLY ACCESS] Upsert instruments

Update or insert one or more instruments into the LUSID instrument master. An instrument will be updated  if it already exists and inserted if it does not.                In the request each instrument definition should be keyed by a unique correlation id. This id is ephemeral  and is not stored by LUSID. It serves only as a way to easily identify each instrument in the response.                The response will return both the collection of successfully updated or inserted instruments, as well as those that failed.  For the failures a reason will be provided explaining why the instrument could not be updated or inserted.                It is important to always check the failed set for any unsuccessful results.  The maximum number of instruments that this method can upsert per request is 2,000.

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

# create an instance of the API class
api_instance = lusid.InstrumentsApi(lusid.ApiClient(configuration))
requests = {'key': lusid.InstrumentDefinition()} # dict(str, InstrumentDefinition) | The definitions of the instruments to update or insert. (optional)

try:
    # [EARLY ACCESS] Upsert instruments
    api_response = api_instance.upsert_instruments(requests=requests)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstrumentsApi->upsert_instruments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requests** | [**dict(str, InstrumentDefinition)**](InstrumentDefinition.md)| The definitions of the instruments to update or insert. | [optional] 

### Return type

[**UpsertInstrumentsResponse**](UpsertInstrumentsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_instruments_properties**
> UpsertInstrumentPropertiesResponse upsert_instruments_properties(instrument_properties)

[EARLY ACCESS] Upsert instruments properties

Update or insert one or more instrument properties for one or more instruments. Each instrument property will be updated  if it already exists and inserted if it does not. If any properties fail to be updated or inserted, none will be updated or inserted and  the reason for the failure will be returned.

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

# create an instance of the API class
api_instance = lusid.InstrumentsApi(lusid.ApiClient(configuration))
instrument_properties = None # list[UpsertInstrumentPropertyRequest] | A collection of instruments and associated instrument properties to update or insert.

try:
    # [EARLY ACCESS] Upsert instruments properties
    api_response = api_instance.upsert_instruments_properties(instrument_properties)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstrumentsApi->upsert_instruments_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_properties** | [**list[UpsertInstrumentPropertyRequest]**](list.md)| A collection of instruments and associated instrument properties to update or insert. | 

### Return type

[**UpsertInstrumentPropertiesResponse**](UpsertInstrumentPropertiesResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

