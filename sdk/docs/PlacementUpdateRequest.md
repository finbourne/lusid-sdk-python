# PlacementUpdateRequest

A request to create or update a Placement.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**quantity** | **float** | The quantity of given instrument ordered. | 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | Client-defined properties associated with this placement. | [optional] 
**counterparty** | **str** | Optionally specifies the market entity this placement is placed with. | [optional] 
**execution_system** | **str** | Optionally specifies the execution system in use. | [optional] 
**entry_type** | **str** | Optionally specifies the entry type of this placement. | [optional] 

## Example

```python
from lusid.models.placement_update_request import PlacementUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PlacementUpdateRequest from a JSON string
placement_update_request_instance = PlacementUpdateRequest.from_json(json)
# print the JSON string representation of the object
print PlacementUpdateRequest.to_json()

# convert the object into a dict
placement_update_request_dict = placement_update_request_instance.to_dict()
# create an instance of PlacementUpdateRequest from a dict
placement_update_request_form_dict = placement_update_request.from_dict(placement_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


