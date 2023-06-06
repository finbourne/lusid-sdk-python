# SubHoldingKeyValueEqualsAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sub_holding_key** | **str** | The sub holding key whose value will form the left-hand side of the operation | 
**value** | **str** | The value to be compared against | 
**criterion_type** | **str** | The available values are: PropertyValueEquals, PropertyValueIn, SubHoldingKeyValueEquals | 

## Example

```python
from lusid.models.sub_holding_key_value_equals_all_of import SubHoldingKeyValueEqualsAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of SubHoldingKeyValueEqualsAllOf from a JSON string
sub_holding_key_value_equals_all_of_instance = SubHoldingKeyValueEqualsAllOf.from_json(json)
# print the JSON string representation of the object
print SubHoldingKeyValueEqualsAllOf.to_json()

# convert the object into a dict
sub_holding_key_value_equals_all_of_dict = sub_holding_key_value_equals_all_of_instance.to_dict()
# create an instance of SubHoldingKeyValueEqualsAllOf from a dict
sub_holding_key_value_equals_all_of_form_dict = sub_holding_key_value_equals_all_of.from_dict(sub_holding_key_value_equals_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


