# LabelValueSet

The set of string labels in a multi-value property.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | **List[str]** |  | 

## Example

```python
from lusid.models.label_value_set import LabelValueSet

# TODO update the JSON string below
json = "{}"
# create an instance of LabelValueSet from a JSON string
label_value_set_instance = LabelValueSet.from_json(json)
# print the JSON string representation of the object
print LabelValueSet.to_json()

# convert the object into a dict
label_value_set_dict = label_value_set_instance.to_dict()
# create an instance of LabelValueSet from a dict
label_value_set_form_dict = label_value_set.from_dict(label_value_set_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


