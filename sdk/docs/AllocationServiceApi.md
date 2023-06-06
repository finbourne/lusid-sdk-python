# lusid.AllocationServiceApi

All URIs are relative to *https://fbn-ci.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**run_allocation_service**](AllocationServiceApi.md#run_allocation_service) | **POST** /api/allocationservice/allocate | [EXPERIMENTAL] RunAllocationService: Runs the Allocation Service


# **run_allocation_service**
> AllocationServiceRunResult run_allocation_service(resource_id, allocation_algorithm=allocation_algorithm)

[EXPERIMENTAL] RunAllocationService: Runs the Allocation Service

This will allocate executions for a given list of placements back to their originating orders.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-ci.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.AllocationServiceApi(api_client)
    resource_id = [{"scope":"MyScope","code":"PLAC00000123"},{"scope":"MyScope","code":"PLAC00000456"}] # List[ResourceId] | The List of Placement IDs for which you wish to allocate executions.
    allocation_algorithm = 'allocation_algorithm_example' # str | A string representation of the allocation algorithm you would like to use to allocate shares from executions e.g. \"PR-FIFO\".  This defaults to \"PR-FIFO\". (optional)

    try:
        # [EXPERIMENTAL] RunAllocationService: Runs the Allocation Service
        api_response = await api_instance.run_allocation_service(resource_id, allocation_algorithm=allocation_algorithm)
        print("The response of AllocationServiceApi->run_allocation_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AllocationServiceApi->run_allocation_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | [**List[ResourceId]**](ResourceId.md)| The List of Placement IDs for which you wish to allocate executions. | 
 **allocation_algorithm** | **str**| A string representation of the allocation algorithm you would like to use to allocate shares from executions e.g. \&quot;PR-FIFO\&quot;.  This defaults to \&quot;PR-FIFO\&quot;. | [optional] 

### Return type

[**AllocationServiceRunResult**](AllocationServiceRunResult.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The results from a run of the Allocation Service |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

