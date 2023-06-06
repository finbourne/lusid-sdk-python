# PropertyValueInAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_key** | **str** | The property key whose value will form the left-hand side of the operation | 
**value** | **List[str]** | The value to be compared against | 
**criterion_type** | **str** | The available values are: PropertyValueEquals, PropertyValueIn, SubHoldingKeyValueEquals | 

## Example

```python
from lusid.models.property_value_in_all_of import PropertyValueInAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyValueInAllOf from a JSON string
property_value_in_all_of_instance = PropertyValueInAllOf.from_json(json)
# print the JSON string representation of the object
print PropertyValueInAllOf.to_json()

# convert the object into a dict
property_value_in_all_of_dict = property_value_in_all_of_instance.to_dict()
# create an instance of PropertyValueInAllOf from a dict
property_value_in_all_of_form_dict = property_value_in_all_of.from_dict(property_value_in_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


