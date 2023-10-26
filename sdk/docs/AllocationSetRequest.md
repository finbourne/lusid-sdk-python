# AllocationSetRequest

A request to create or update multiple Allocations.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocation_requests** | [**List[AllocationRequest]**](AllocationRequest.md) | A collection of AllocationRequests. | [optional] 

## Example

```python
from lusid.models.allocation_set_request import AllocationSetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AllocationSetRequest from a JSON string
allocation_set_request_instance = AllocationSetRequest.from_json(json)
# print the JSON string representation of the object
print AllocationSetRequest.to_json()

# convert the object into a dict
allocation_set_request_dict = allocation_set_request_instance.to_dict()
# create an instance of AllocationSetRequest from a dict
allocation_set_request_form_dict = allocation_set_request.from_dict(allocation_set_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


