# PropertyValueEquals

A criterion that checks whether a Property Value is equal to the given string value

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_key** | **str** | The property key whose value will form the left-hand side of the operation | 
**value** | **str** | The value to be compared against | 
**criterion_type** | **str** | The available values are: PropertyValueEquals, PropertyValueIn, SubHoldingKeyValueEquals | 

## Example

```python
from lusid.models.property_value_equals import PropertyValueEquals

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyValueEquals from a JSON string
property_value_equals_instance = PropertyValueEquals.from_json(json)
# print the JSON string representation of the object
print PropertyValueEquals.to_json()

# convert the object into a dict
property_value_equals_dict = property_value_equals_instance.to_dict()
# create an instance of PropertyValueEquals from a dict
property_value_equals_form_dict = property_value_equals.from_dict(property_value_equals_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


