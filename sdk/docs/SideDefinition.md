# SideDefinition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**side** | **str** | A unique label identifying the side definition. | 
**security** | **str** | The field or property key defining the side&#39;s security, or instrument. | 
**currency** | **str** | The field or property key defining the side&#39;s currency. | 
**rate** | **str** | The field or property key defining the side&#39;s rate. | 
**units** | **str** | The value, field or property key defining the side&#39;s units. | 
**amount** | **str** | The value, field or property key defining the side&#39;s amount | 
**notional_amount** | **str** | The value, field or property key defining the side&#39;s notional amount | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.side_definition import SideDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of SideDefinition from a JSON string
side_definition_instance = SideDefinition.from_json(json)
# print the JSON string representation of the object
print SideDefinition.to_json()

# convert the object into a dict
side_definition_dict = side_definition_instance.to_dict()
# create an instance of SideDefinition from a dict
side_definition_form_dict = side_definition.from_dict(side_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


