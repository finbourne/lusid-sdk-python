# AllocationServiceRunResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[ResourceId]**](ResourceId.md) |  | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) |  | [optional] 

## Example

```python
from lusid.models.allocation_service_run_response import AllocationServiceRunResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AllocationServiceRunResponse from a JSON string
allocation_service_run_response_instance = AllocationServiceRunResponse.from_json(json)
# print the JSON string representation of the object
print AllocationServiceRunResponse.to_json()

# convert the object into a dict
allocation_service_run_response_dict = allocation_service_run_response_instance.to_dict()
# create an instance of AllocationServiceRunResponse from a dict
allocation_service_run_response_form_dict = allocation_service_run_response.from_dict(allocation_service_run_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


