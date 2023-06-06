# SupportedAnalyticsInternalRequest

The request body for the SupportedAnalyticsInternal endpoint

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_all_addresses** | **bool** | If true, then we show every possible address key, otherwise we show the address keys specified in addresses array. | 
**addresses** | **List[str]** | Address keys specified here will be included in the response to the call, which will include details on whether those keys are supported. | [optional] 
**group_by** | **List[str]** | The address keys to group by. | 
**show_test_counts** | **bool** | If true, returns an integer matrix showing test counts for each address.  If false, masks to a boolean matrix representing whether an address is supported or unsupported. | [optional] 

## Example

```python
from lusid.models.supported_analytics_internal_request import SupportedAnalyticsInternalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SupportedAnalyticsInternalRequest from a JSON string
supported_analytics_internal_request_instance = SupportedAnalyticsInternalRequest.from_json(json)
# print the JSON string representation of the object
print SupportedAnalyticsInternalRequest.to_json()

# convert the object into a dict
supported_analytics_internal_request_dict = supported_analytics_internal_request_instance.to_dict()
# create an instance of SupportedAnalyticsInternalRequest from a dict
supported_analytics_internal_request_form_dict = supported_analytics_internal_request.from_dict(supported_analytics_internal_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


