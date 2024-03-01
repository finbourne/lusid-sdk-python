# ComponentTransaction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** |  | 
**condition** | **str** |  | [optional] 
**transaction_field_map** | [**TransactionFieldMap**](TransactionFieldMap.md) |  | 
**transaction_property_map** | [**List[TransactionPropertyMap]**](TransactionPropertyMap.md) |  | 

## Example

```python
from lusid.models.component_transaction import ComponentTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of ComponentTransaction from a JSON string
component_transaction_instance = ComponentTransaction.from_json(json)
# print the JSON string representation of the object
print ComponentTransaction.to_json()

# convert the object into a dict
component_transaction_dict = component_transaction_instance.to_dict()
# create an instance of ComponentTransaction from a dict
component_transaction_form_dict = component_transaction.from_dict(component_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


