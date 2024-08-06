# SideDefinitionRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**security** | **str** | The field or property key defining the side&#39;s security, or instrument. | 
**currency** | **str** | The field or property key defining the side&#39;s currency. | 
**rate** | **str** | The field or property key defining the side&#39;s rate. | 
**units** | **str** | The value, field or property key defining the side&#39;s units. | 
**amount** | **str** | The value, field or property key defining the side&#39;s amount | 
**notional_amount** | **str** | The value, field or property key defining the side&#39;s notional amount | [optional] 

## Example

```python
from lusid.models.side_definition_request import SideDefinitionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SideDefinitionRequest from a JSON string
side_definition_request_instance = SideDefinitionRequest.from_json(json)
# print the JSON string representation of the object
print SideDefinitionRequest.to_json()

# convert the object into a dict
side_definition_request_dict = side_definition_request_instance.to_dict()
# create an instance of SideDefinitionRequest from a dict
side_definition_request_form_dict = side_definition_request.from_dict(side_definition_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


