# TransactionPropertyMappingRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_key** | **str** | Uniquely identifies the property definition and consists of a Domain, Scope and Code. | 
**map_from** | **str** | The Property Key of the Property to map from. | [optional] 
**set_to** | **object** | A pointer to the Property being mapped from. | [optional] 

## Example

```python
from lusid.models.transaction_property_mapping_request import TransactionPropertyMappingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionPropertyMappingRequest from a JSON string
transaction_property_mapping_request_instance = TransactionPropertyMappingRequest.from_json(json)
# print the JSON string representation of the object
print TransactionPropertyMappingRequest.to_json()

# convert the object into a dict
transaction_property_mapping_request_dict = transaction_property_mapping_request_instance.to_dict()
# create an instance of TransactionPropertyMappingRequest from a dict
transaction_property_mapping_request_form_dict = transaction_property_mapping_request.from_dict(transaction_property_mapping_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


