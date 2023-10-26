# CompositeBreakdownResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**results** | **Dict[str, List[CompositeBreakdown]]** | The Composite calculation with the constituens which were included. | 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.composite_breakdown_response import CompositeBreakdownResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CompositeBreakdownResponse from a JSON string
composite_breakdown_response_instance = CompositeBreakdownResponse.from_json(json)
# print the JSON string representation of the object
print CompositeBreakdownResponse.to_json()

# convert the object into a dict
composite_breakdown_response_dict = composite_breakdown_response_instance.to_dict()
# create an instance of CompositeBreakdownResponse from a dict
composite_breakdown_response_form_dict = composite_breakdown_response.from_dict(composite_breakdown_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


