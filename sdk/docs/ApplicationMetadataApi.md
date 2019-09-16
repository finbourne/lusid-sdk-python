# lusid.ApplicationMetadataApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_excel_addin**](ApplicationMetadataApi.md#get_excel_addin) | **GET** /api/metadata/downloads/exceladdin | [EARLY ACCESS] Download Excel Addin
[**get_lusid_versions**](ApplicationMetadataApi.md#get_lusid_versions) | **GET** /api/metadata/versions | [EARLY ACCESS] Get LUSID versions
[**list_access_controlled_resources**](ApplicationMetadataApi.md#list_access_controlled_resources) | **GET** /api/metadata/access/resources | [EARLY ACCESS] Get resources available for access control


# **get_excel_addin**
> FileResponse get_excel_addin(version=version)

[EARLY ACCESS] Download Excel Addin

Download the LUSID Excel Addin for Microsoft Excel. Not providing a specific value will return the latest version being returned

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

# Defining host is optional and default to http://localhost/api
configuration.host = "http://localhost/api"
# Create an instance of the API class
api_instance = lusid.ApplicationMetadataApi(lusid.ApiClient(configuration))
version = 'version_example' # str | The requested version of the Excel plugin (optional)

try:
    # [EARLY ACCESS] Download Excel Addin
    api_response = api_instance.get_excel_addin(version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationMetadataApi->get_excel_addin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| The requested version of the Excel plugin | [optional] 

### Return type

[**FileResponse**](FileResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lusid_versions**
> VersionSummaryDto get_lusid_versions()

[EARLY ACCESS] Get LUSID versions

Get the semantic versions associated with LUSID and its ecosystem

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

# Defining host is optional and default to http://localhost/api
configuration.host = "http://localhost/api"
# Create an instance of the API class
api_instance = lusid.ApplicationMetadataApi(lusid.ApiClient(configuration))

try:
    # [EARLY ACCESS] Get LUSID versions
    api_response = api_instance.get_lusid_versions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationMetadataApi->get_lusid_versions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**VersionSummaryDto**](VersionSummaryDto.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Collection of versions associated with LUSID |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_access_controlled_resources**
> ResourceListOfAccessControlledResource list_access_controlled_resources(filter=filter)

[EARLY ACCESS] Get resources available for access control

Get the comprehensive set of resources that are available for access control

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

# Defining host is optional and default to http://localhost/api
configuration.host = "http://localhost/api"
# Create an instance of the API class
api_instance = lusid.ApplicationMetadataApi(lusid.ApiClient(configuration))
filter = 'filter_example' # str | Optional. Expression to filter the result set (optional)

try:
    # [EARLY ACCESS] Get resources available for access control
    api_response = api_instance.list_access_controlled_resources(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationMetadataApi->list_access_controlled_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Optional. Expression to filter the result set | [optional] 

### Return type

[**ResourceListOfAccessControlledResource**](ResourceListOfAccessControlledResource.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

