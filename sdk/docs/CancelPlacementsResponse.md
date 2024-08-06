# CancelPlacementsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**values** | [**Dict[str, CancelledPlacementResult]**](CancelledPlacementResult.md) | The placements which have been successfully cancelled. | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The placements that could not be cancelled, along with a reason for their failure. | [optional] 
**metadata** | **Dict[str, List[ResponseMetaData]]** | Meta data associated with the cancellation event. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.cancel_placements_response import CancelPlacementsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CancelPlacementsResponse from a JSON string
cancel_placements_response_instance = CancelPlacementsResponse.from_json(json)
# print the JSON string representation of the object
print CancelPlacementsResponse.to_json()

# convert the object into a dict
cancel_placements_response_dict = cancel_placements_response_instance.to_dict()
# create an instance of CancelPlacementsResponse from a dict
cancel_placements_response_form_dict = cancel_placements_response.from_dict(cancel_placements_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


