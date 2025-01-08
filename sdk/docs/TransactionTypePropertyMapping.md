# TransactionTypePropertyMapping


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_key** | **str** | The key that uniquely identifies the property. It has the format {domain}/{scope}/{code} | 
**map_from** | **str** | The Property Key of the Property to map from | [optional] 
**set_to** | **str** | A pointer to the Property being mapped from | [optional] 
**template_from** | **str** | The template that defines how the property value is constructed from transaction, instrument and portfolio details. | [optional] 

## Example

```python
from lusid.models.transaction_type_property_mapping import TransactionTypePropertyMapping

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionTypePropertyMapping from a JSON string
transaction_type_property_mapping_instance = TransactionTypePropertyMapping.from_json(json)
# print the JSON string representation of the object
print TransactionTypePropertyMapping.to_json()

# convert the object into a dict
transaction_type_property_mapping_dict = transaction_type_property_mapping_instance.to_dict()
# create an instance of TransactionTypePropertyMapping from a dict
transaction_type_property_mapping_form_dict = transaction_type_property_mapping.from_dict(transaction_type_property_mapping_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


