# lusid.LoginApi

All URIs are relative to *http://local-unit-test-server.lusid.com:60304*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_saml_identity_provider_id**](LoginApi.md#get_saml_identity_provider_id) | **GET** /api/login/saml/{domain} | Get SAML Identity Provider


# **get_saml_identity_provider_id**
> str get_saml_identity_provider_id(domain)

Get SAML Identity Provider

Get the unique identifier for the SAML 2.0 Identity Provider to be used for domain.

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

# Defining host is optional and default to http://local-unit-test-server.lusid.com:60304
configuration.host = "http://local-unit-test-server.lusid.com:60304"
# Create an instance of the API class
api_instance = lusid.LoginApi(lusid.ApiClient(configuration))
domain = 'domain_example' # str | The domain that the user will be logging in to

try:
    # Get SAML Identity Provider
    api_response = api_instance.get_saml_identity_provider_id(domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoginApi->get_saml_identity_provider_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain that the user will be logging in to | 

### Return type

**str**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The ID of the SAML Identity Provider to be used (may be null) |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

