# TransactionPropertyMapping


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_key** | **str** | The key that uniquely identifies the property. It has the format {domain}/{scope}/{code} | 
**map_from** | **str** | The Property Key of the Property to map from | [optional] 
**set_to** | **object** | A pointer to the Property being mapped from | [optional] 

## Example

```python
from lusid.models.transaction_property_mapping import TransactionPropertyMapping

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionPropertyMapping from a JSON string
transaction_property_mapping_instance = TransactionPropertyMapping.from_json(json)
# print the JSON string representation of the object
print TransactionPropertyMapping.to_json()

# convert the object into a dict
transaction_property_mapping_dict = transaction_property_mapping_instance.to_dict()
# create an instance of TransactionPropertyMapping from a dict
transaction_property_mapping_form_dict = transaction_property_mapping.from_dict(transaction_property_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


