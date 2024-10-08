# ComparisonAttributeValuePair


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_name** | **str** | Comparison rule attribute name. | 
**value** | **str** | Computed value for the comparison rule attribute. | 

## Example

```python
from lusid.models.comparison_attribute_value_pair import ComparisonAttributeValuePair

# TODO update the JSON string below
json = "{}"
# create an instance of ComparisonAttributeValuePair from a JSON string
comparison_attribute_value_pair_instance = ComparisonAttributeValuePair.from_json(json)
# print the JSON string representation of the object
print ComparisonAttributeValuePair.to_json()

# convert the object into a dict
comparison_attribute_value_pair_dict = comparison_attribute_value_pair_instance.to_dict()
# create an instance of ComparisonAttributeValuePair from a dict
comparison_attribute_value_pair_form_dict = comparison_attribute_value_pair.from_dict(comparison_attribute_value_pair_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


