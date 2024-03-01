# TransactionPropertyMap


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_key** | **str** | The key that uniquely identifies the property. It has the format {domain}/{scope}/{code}. | [optional] 
**property_value** | [**PropertyValue**](PropertyValue.md) |  | [optional] 

## Example

```python
from lusid.models.transaction_property_map import TransactionPropertyMap

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionPropertyMap from a JSON string
transaction_property_map_instance = TransactionPropertyMap.from_json(json)
# print the JSON string representation of the object
print TransactionPropertyMap.to_json()

# convert the object into a dict
transaction_property_map_dict = transaction_property_map_instance.to_dict()
# create an instance of TransactionPropertyMap from a dict
transaction_property_map_form_dict = transaction_property_map.from_dict(transaction_property_map_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


