# AddressKeyOptionDefinition

The definition of an Address Key Option

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the option | 
**type** | **str** | The type of the option | 
**description** | **str** | The description of the option | 
**optional** | **bool** | Is this option required or optional? | 
**allowed_value_set** | **List[str]** | If the option is a string or enum, the allowed set of values it can take. | [optional] 
**default_value** | **str** | If the option is not required, what is the default value? | [optional] 

## Example

```python
from lusid.models.address_key_option_definition import AddressKeyOptionDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of AddressKeyOptionDefinition from a JSON string
address_key_option_definition_instance = AddressKeyOptionDefinition.from_json(json)
# print the JSON string representation of the object
print AddressKeyOptionDefinition.to_json()

# convert the object into a dict
address_key_option_definition_dict = address_key_option_definition_instance.to_dict()
# create an instance of AddressKeyOptionDefinition from a dict
address_key_option_definition_form_dict = address_key_option_definition.from_dict(address_key_option_definition_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


