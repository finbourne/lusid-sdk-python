# lusid.ApplicationMetadataApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_excel_addin**](ApplicationMetadataApi.md#get_excel_addin) | **GET** /api/metadata/downloads/exceladdin | Download Excel Addin
[**get_excel_download_url**](ApplicationMetadataApi.md#get_excel_download_url) | **GET** /api/metadata/downloads/excel | Get Excel download url
[**get_lusid_versions**](ApplicationMetadataApi.md#get_lusid_versions) | **GET** /api/metadata/versions | Get LUSID versions


# **get_excel_addin**
> FileResponse get_excel_addin(version=version)

Download Excel Addin

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

# create an instance of the API class
api_instance = lusid.ApplicationMetadataApi(lusid.ApiClient(configuration))
version = 'version_example' # str | The requested version of the Excel plugin (optional)

try:
    # Download Excel Addin
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_excel_download_url**
> str get_excel_download_url(version=version)

Get Excel download url

Request an authorised url for an Excel client version

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
api_instance = lusid.ApplicationMetadataApi(lusid.ApiClient(configuration))
version = 'version_example' # str | The requested version of the Excel plugin (optional)

try:
    # Get Excel download url
    api_response = api_instance.get_excel_download_url(version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationMetadataApi->get_excel_download_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| The requested version of the Excel plugin | [optional] 

### Return type

**str**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lusid_versions**
> VersionSummaryDto get_lusid_versions()

Get LUSID versions

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

# create an instance of the API class
api_instance = lusid.ApplicationMetadataApi(lusid.ApiClient(configuration))

try:
    # Get LUSID versions
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

