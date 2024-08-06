# FieldValue


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | 
**fields** | **Dict[str, str]** |  | 

## Example

```python
from lusid.models.field_value import FieldValue

# TODO update the JSON string below
json = "{}"
# create an instance of FieldValue from a JSON string
field_value_instance = FieldValue.from_json(json)
# print the JSON string representation of the object
print FieldValue.to_json()

# convert the object into a dict
field_value_dict = field_value_instance.to_dict()
# create an instance of FieldValue from a dict
field_value_form_dict = field_value.from_dict(field_value_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


