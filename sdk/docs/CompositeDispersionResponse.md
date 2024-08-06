# CompositeDispersionResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**results** | **Dict[str, List[CompositeDispersion]]** | Dispersion returns calculation grouped by ReturnId | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.composite_dispersion_response import CompositeDispersionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CompositeDispersionResponse from a JSON string
composite_dispersion_response_instance = CompositeDispersionResponse.from_json(json)
# print the JSON string representation of the object
print CompositeDispersionResponse.to_json()

# convert the object into a dict
composite_dispersion_response_dict = composite_dispersion_response_instance.to_dict()
# create an instance of CompositeDispersionResponse from a dict
composite_dispersion_response_form_dict = composite_dispersion_response.from_dict(composite_dispersion_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


