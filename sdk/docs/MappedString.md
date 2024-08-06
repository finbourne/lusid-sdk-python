# MappedString


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left_value** | **str** |  | [optional] 
**right_value** | **str** |  | [optional] 
**mapping_direction** | **str** |  | [optional] 
**is_case_sensitive** | **bool** |  | [optional] 

## Example

```python
from lusid.models.mapped_string import MappedString

# TODO update the JSON string below
json = "{}"
# create an instance of MappedString from a JSON string
mapped_string_instance = MappedString.from_json(json)
# print the JSON string representation of the object
print MappedString.to_json()

# convert the object into a dict
mapped_string_dict = mapped_string_instance.to_dict()
# create an instance of MappedString from a dict
mapped_string_form_dict = mapped_string.from_dict(mapped_string_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


