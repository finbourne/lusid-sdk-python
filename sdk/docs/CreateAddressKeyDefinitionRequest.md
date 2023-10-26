# CreateAddressKeyDefinitionRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_key** | **str** | The address key of the address key definition. | 
**type** | **str** | The type of the address key definition | 

## Example

```python
from lusid.models.create_address_key_definition_request import CreateAddressKeyDefinitionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAddressKeyDefinitionRequest from a JSON string
create_address_key_definition_request_instance = CreateAddressKeyDefinitionRequest.from_json(json)
# print the JSON string representation of the object
print CreateAddressKeyDefinitionRequest.to_json()

# convert the object into a dict
create_address_key_definition_request_dict = create_address_key_definition_request_instance.to_dict()
# create an instance of CreateAddressKeyDefinitionRequest from a dict
create_address_key_definition_request_form_dict = create_address_key_definition_request.from_dict(create_address_key_definition_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


