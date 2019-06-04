# lusid.InstrumentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_instrument**](InstrumentsApi.md#delete_instrument) | **DELETE** /api/instruments/{identifierType}/{identifier} | Delete instrument
[**get_instrument**](InstrumentsApi.md#get_instrument) | **GET** /api/instruments/{identifierType}/{identifier} | Get instrument definition
[**get_instrument_identifiers**](InstrumentsApi.md#get_instrument_identifiers) | **GET** /api/instruments/identifiers | Get allowable instrument identifiers
[**get_instruments**](InstrumentsApi.md#get_instruments) | **POST** /api/instruments/$get | Get instrument definition
[**list_instruments**](InstrumentsApi.md#list_instruments) | **GET** /api/instruments | Get all of the currently mastered instruments in LUSID
[**update_instrument_identifier**](InstrumentsApi.md#update_instrument_identifier) | **POST** /api/instruments/{identifierType}/{identifier} | Update instrument identifier
[**upsert_instruments**](InstrumentsApi.md#upsert_instruments) | **POST** /api/instruments | Upsert instruments
[**upsert_instruments_properties**](InstrumentsApi.md#upsert_instruments_properties) | **POST** /api/instruments/$upsertproperties | Upsert instrument properties


# **delete_instrument**
> DeleteInstrumentResponse delete_instrument(identifier_type, identifier)

Delete instrument

Attempt to delete one or more \"client\" instruments.    The response will include those instruments that could not be deleted (as well as any available details).                It is important to always check the 'Failed' set for any unsuccessful results.

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
identifier_type = 'identifier_type_example' # str | The type of identifier being supplied
identifier = 'identifier_example' # str | The instrument identifier

try:
    # Delete instrument
    api_response = api_instance.delete_instrument(identifier_type, identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstrumentsApi->delete_instrument: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier_type** | **str**| The type of identifier being supplied | 
 **identifier** | **str**| The instrument identifier | 

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

Get instrument definition

Get an individual instrument by the one of its unique instrument identifiers. Optionally, it is possible to decorate each instrument with specified property data.

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
identifier_type = 'identifier_type_example' # str | The type of identifier being supplied
identifier = 'identifier_example' # str | The identifier of the requested instrument
effective_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The effective date of the query (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The AsAt date of the query (optional)
instrument_property_keys = ['instrument_property_keys_example'] # list[str] | Optional. Keys of the properties to be decorated on to the instrument (optional)

try:
    # Get instrument definition
    api_response = api_instance.get_instrument(identifier_type, identifier, effective_at=effective_at, as_at=as_at, instrument_property_keys=instrument_property_keys)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstrumentsApi->get_instrument: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier_type** | **str**| The type of identifier being supplied | 
 **identifier** | **str**| The identifier of the requested instrument | 
 **effective_at** | **datetime**| Optional. The effective date of the query | [optional] 
 **as_at** | **datetime**| Optional. The AsAt date of the query | [optional] 
 **instrument_property_keys** | [**list[str]**](str.md)| Optional. Keys of the properties to be decorated on to the instrument | [optional] 

### Return type

[**Instrument**](Instrument.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_instrument_identifiers**
> ResourceListOfInstrumentIdTypeDescriptor get_instrument_identifiers()

Get allowable instrument identifiers

Returns a collection of instrument identifier type descriptors. Each descriptor specifies the properties  of a particular instrument identifier - its name, its cardinality (whether or not multiple instruments can  share the same identifier value), and its corresponding PropertyKey.

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
    # Get allowable instrument identifiers
    api_response = api_instance.get_instrument_identifiers()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstrumentsApi->get_instrument_identifiers: %s\n" % e)
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

Get instrument definition

Get a collection of instruments by a set of identifiers. Optionally, it is possible to decorate each instrument with specified property data.

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
identifier_type = 'identifier_type_example' # str | The type of identifiers being supplied
identifiers = None # list[str] | The identifiers of the instruments to get
effective_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The effective date of the request (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The as at date of the request (optional)
instrument_property_keys = ['instrument_property_keys_example'] # list[str] | Optional. Keys of the properties to be decorated on to the instrument (optional)

try:
    # Get instrument definition
    api_response = api_instance.get_instruments(identifier_type, identifiers, effective_at=effective_at, as_at=as_at, instrument_property_keys=instrument_property_keys)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstrumentsApi->get_instruments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier_type** | **str**| The type of identifiers being supplied | 
 **identifiers** | [**list[str]**](list.md)| The identifiers of the instruments to get | 
 **effective_at** | **datetime**| Optional. The effective date of the request | [optional] 
 **as_at** | **datetime**| Optional. The as at date of the request | [optional] 
 **instrument_property_keys** | [**list[str]**](str.md)| Optional. Keys of the properties to be decorated on to the instrument | [optional] 

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

Get all of the currently mastered instruments in LUSID

Lists all instruments that have been mastered within LUSID.

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
as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The AsAt time (optional)
effective_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The effective date of the query (optional)
page = 'page_example' # str | Optional. The pagination token to continue listing instruments. This value is returned from a previous call to ListInstruments.  If this is set, then the sortBy, filter, effectiveAt, and asAt fields must not have changed. Also, if set, a start value cannot be set. (optional)
sort_by = ['sort_by_example'] # list[str] | Optional. Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName (optional)
start = 56 # int | Optional. When paginating, skip this number of results (optional)
limit = 56 # int | Optional. When paginating, limit the number of returned results to this many (optional)
filter = 'State eq 'Active'' # str | Optional. Expression to filter the result set - the default filter returns only instruments in the Active state (optional) (default to 'State eq 'Active'')
instrument_property_keys = ['instrument_property_keys_example'] # list[str] | Optional. Keys of the properties to be decorated on to the instrument (optional)

try:
    # Get all of the currently mastered instruments in LUSID
    api_response = api_instance.list_instruments(as_at=as_at, effective_at=effective_at, page=page, sort_by=sort_by, start=start, limit=limit, filter=filter, instrument_property_keys=instrument_property_keys)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstrumentsApi->list_instruments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| Optional. The AsAt time | [optional] 
 **effective_at** | **datetime**| Optional. The effective date of the query | [optional] 
 **page** | **str**| Optional. The pagination token to continue listing instruments. This value is returned from a previous call to ListInstruments.  If this is set, then the sortBy, filter, effectiveAt, and asAt fields must not have changed. Also, if set, a start value cannot be set. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Optional. Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName | [optional] 
 **start** | **int**| Optional. When paginating, skip this number of results | [optional] 
 **limit** | **int**| Optional. When paginating, limit the number of returned results to this many | [optional] 
 **filter** | **str**| Optional. Expression to filter the result set - the default filter returns only instruments in the Active state | [optional] [default to &#39;State eq &#39;Active&#39;&#39;]
 **instrument_property_keys** | [**list[str]**](str.md)| Optional. Keys of the properties to be decorated on to the instrument | [optional] 

### Return type

[**ResourceListOfInstrument**](ResourceListOfInstrument.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_instrument_identifier**
> Instrument update_instrument_identifier(identifier_type, identifier, request=request)

Update instrument identifier

Adds, updates, or removes an identifier on an instrument

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
identifier_type = 'identifier_type_example' # str | The type of identifier being supplied
identifier = 'identifier_example' # str | The instrument identifier
request = lusid.UpdateInstrumentIdentifierRequest() # UpdateInstrumentIdentifierRequest | The identifier to add, update, or remove (optional)

try:
    # Update instrument identifier
    api_response = api_instance.update_instrument_identifier(identifier_type, identifier, request=request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstrumentsApi->update_instrument_identifier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier_type** | **str**| The type of identifier being supplied | 
 **identifier** | **str**| The instrument identifier | 
 **request** | [**UpdateInstrumentIdentifierRequest**](UpdateInstrumentIdentifierRequest.md)| The identifier to add, update, or remove | [optional] 

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

Upsert instruments

Attempt to master one or more instruments in LUSID's instrument master. Each instrument is keyed by some unique key. This key is unimportant, and serves only as a method to identify created instruments in the response.    The response will return both the collection of successfully created instruments, as well as those that were rejected and why their creation failed. They will be keyed against the key supplied in the  request.                It is important to always check the 'Failed' set for any unsuccessful results.

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
requests = {'key': lusid.InstrumentDefinition()} # dict(str, InstrumentDefinition) | The instrument definitions (optional)

try:
    # Upsert instruments
    api_response = api_instance.upsert_instruments(requests=requests)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstrumentsApi->upsert_instruments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requests** | [**dict(str, InstrumentDefinition)**](InstrumentDefinition.md)| The instrument definitions | [optional] 

### Return type

[**UpsertInstrumentsResponse**](UpsertInstrumentsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_instruments_properties**
> UpsertInstrumentPropertiesResponse upsert_instruments_properties(instrument_properties=instrument_properties)

Upsert instrument properties

Attempt to upsert property data for one or more instruments, properties, and effective dates.    The response will include the details of any failures that occurred during data storage.                It is important to always check the 'Failed' collection for any unsuccessful results.

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
instrument_properties = None # list[UpsertInstrumentPropertyRequest] | The instrument property data (optional)

try:
    # Upsert instrument properties
    api_response = api_instance.upsert_instruments_properties(instrument_properties=instrument_properties)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstrumentsApi->upsert_instruments_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_properties** | [**list[UpsertInstrumentPropertyRequest]**](list.md)| The instrument property data | [optional] 

### Return type

[**UpsertInstrumentPropertiesResponse**](UpsertInstrumentPropertiesResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

