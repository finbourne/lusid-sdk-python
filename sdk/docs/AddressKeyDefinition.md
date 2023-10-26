# AddressKeyDefinition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_key** | **str** | The address key of the address key definition. | 
**type** | **str** | The type of the address key definition | 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.address_key_definition import AddressKeyDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of AddressKeyDefinition from a JSON string
address_key_definition_instance = AddressKeyDefinition.from_json(json)
# print the JSON string representation of the object
print AddressKeyDefinition.to_json()

# convert the object into a dict
address_key_definition_dict = address_key_definition_instance.to_dict()
# create an instance of AddressKeyDefinition from a dict
address_key_definition_form_dict = address_key_definition.from_dict(address_key_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


