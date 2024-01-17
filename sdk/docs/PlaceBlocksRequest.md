# PlaceBlocksRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | [**List[PlacementRequest]**](PlacementRequest.md) | A collection of PlacementRequest. | 

## Example

```python
from lusid.models.place_blocks_request import PlaceBlocksRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PlaceBlocksRequest from a JSON string
place_blocks_request_instance = PlaceBlocksRequest.from_json(json)
# print the JSON string representation of the object
print PlaceBlocksRequest.to_json()

# convert the object into a dict
place_blocks_request_dict = place_blocks_request_instance.to_dict()
# create an instance of PlaceBlocksRequest from a dict
place_blocks_request_form_dict = place_blocks_request.from_dict(place_blocks_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


