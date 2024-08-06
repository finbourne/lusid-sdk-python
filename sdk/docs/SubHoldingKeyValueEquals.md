# SubHoldingKeyValueEquals

A criterion that checks whether a SubHoldingKey Value is equal to the given string value

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sub_holding_key** | **str** | The sub holding key whose value will form the left-hand side of the operation | 
**value** | **str** | The value to be compared against | 
**criterion_type** | **str** | The available values are: PropertyValueEquals, PropertyValueIn, SubHoldingKeyValueEquals | 

## Example

```python
from lusid.models.sub_holding_key_value_equals import SubHoldingKeyValueEquals

# TODO update the JSON string below
json = "{}"
# create an instance of SubHoldingKeyValueEquals from a JSON string
sub_holding_key_value_equals_instance = SubHoldingKeyValueEquals.from_json(json)
# print the JSON string representation of the object
print SubHoldingKeyValueEquals.to_json()

# convert the object into a dict
sub_holding_key_value_equals_dict = sub_holding_key_value_equals_instance.to_dict()
# create an instance of SubHoldingKeyValueEquals from a dict
sub_holding_key_value_equals_form_dict = sub_holding_key_value_equals.from_dict(sub_holding_key_value_equals_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


