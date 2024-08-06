# FieldDefinition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**is_required** | **bool** |  | 
**is_unique** | **bool** |  | 

## Example

```python
from lusid.models.field_definition import FieldDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of FieldDefinition from a JSON string
field_definition_instance = FieldDefinition.from_json(json)
# print the JSON string representation of the object
print FieldDefinition.to_json()

# convert the object into a dict
field_definition_dict = field_definition_instance.to_dict()
# create an instance of FieldDefinition from a dict
field_definition_form_dict = field_definition.from_dict(field_definition_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


