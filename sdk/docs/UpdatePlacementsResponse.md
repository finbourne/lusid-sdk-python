# UpdatePlacementsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**values** | [**Dict[str, Placement]**](Placement.md) | The placements which have been successfully updated. | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The placements that could not be updated, along with a reason for their failure. | [optional] 
**metadata** | **Dict[str, List[ResponseMetaData]]** | Meta data associated with the update event. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.update_placements_response import UpdatePlacementsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePlacementsResponse from a JSON string
update_placements_response_instance = UpdatePlacementsResponse.from_json(json)
# print the JSON string representation of the object
print UpdatePlacementsResponse.to_json()

# convert the object into a dict
update_placements_response_dict = update_placements_response_instance.to_dict()
# create an instance of UpdatePlacementsResponse from a dict
update_placements_response_form_dict = update_placements_response.from_dict(update_placements_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


