# SidesDefinitionRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**side** | **str** | A unique label identifying the side definition. | 
**side_request** | [**SideDefinitionRequest**](SideDefinitionRequest.md) |  | 

## Example

```python
from lusid.models.sides_definition_request import SidesDefinitionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SidesDefinitionRequest from a JSON string
sides_definition_request_instance = SidesDefinitionRequest.from_json(json)
# print the JSON string representation of the object
print SidesDefinitionRequest.to_json()

# convert the object into a dict
sides_definition_request_dict = sides_definition_request_instance.to_dict()
# create an instance of SidesDefinitionRequest from a dict
sides_definition_request_form_dict = sides_definition_request.from_dict(sides_definition_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


