# IdentifierPartSchema


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** |  | 
**name** | **str** |  | 
**display_name** | **str** |  | 
**description** | **str** |  | 
**required** | **bool** |  | 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.identifier_part_schema import IdentifierPartSchema

# TODO update the JSON string below
json = "{}"
# create an instance of IdentifierPartSchema from a JSON string
identifier_part_schema_instance = IdentifierPartSchema.from_json(json)
# print the JSON string representation of the object
print IdentifierPartSchema.to_json()

# convert the object into a dict
identifier_part_schema_dict = identifier_part_schema_instance.to_dict()
# create an instance of IdentifierPartSchema from a dict
identifier_part_schema_form_dict = identifier_part_schema.from_dict(identifier_part_schema_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


