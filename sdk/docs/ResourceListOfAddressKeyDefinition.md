# ResourceListOfAddressKeyDefinition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[AddressKeyDefinition]**](AddressKeyDefinition.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid.models.resource_list_of_address_key_definition import ResourceListOfAddressKeyDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfAddressKeyDefinition from a JSON string
resource_list_of_address_key_definition_instance = ResourceListOfAddressKeyDefinition.from_json(json)
# print the JSON string representation of the object
print ResourceListOfAddressKeyDefinition.to_json()

# convert the object into a dict
resource_list_of_address_key_definition_dict = resource_list_of_address_key_definition_instance.to_dict()
# create an instance of ResourceListOfAddressKeyDefinition from a dict
resource_list_of_address_key_definition_form_dict = resource_list_of_address_key_definition.from_dict(resource_list_of_address_key_definition_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


