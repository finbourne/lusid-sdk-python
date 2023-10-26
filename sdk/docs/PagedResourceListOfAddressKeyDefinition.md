# PagedResourceListOfAddressKeyDefinition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**values** | [**List[AddressKeyDefinition]**](AddressKeyDefinition.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.paged_resource_list_of_address_key_definition import PagedResourceListOfAddressKeyDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResourceListOfAddressKeyDefinition from a JSON string
paged_resource_list_of_address_key_definition_instance = PagedResourceListOfAddressKeyDefinition.from_json(json)
# print the JSON string representation of the object
print PagedResourceListOfAddressKeyDefinition.to_json()

# convert the object into a dict
paged_resource_list_of_address_key_definition_dict = paged_resource_list_of_address_key_definition_instance.to_dict()
# create an instance of PagedResourceListOfAddressKeyDefinition from a dict
paged_resource_list_of_address_key_definition_form_dict = paged_resource_list_of_address_key_definition.from_dict(paged_resource_list_of_address_key_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


