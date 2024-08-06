# PlacementSetRequest

A request to create or update multiple Placements.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | [**List[PlacementRequest]**](PlacementRequest.md) | A collection of PlacementRequests. | [optional] 

## Example

```python
from lusid.models.placement_set_request import PlacementSetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PlacementSetRequest from a JSON string
placement_set_request_instance = PlacementSetRequest.from_json(json)
# print the JSON string representation of the object
print PlacementSetRequest.to_json()

# convert the object into a dict
placement_set_request_dict = placement_set_request_instance.to_dict()
# create an instance of PlacementSetRequest from a dict
placement_set_request_form_dict = placement_set_request.from_dict(placement_set_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


