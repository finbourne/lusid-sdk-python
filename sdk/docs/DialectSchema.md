# DialectSchema

A schema that a given document must obey. A representation of the validation of a particular Dialect,  in a given language.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of schema this represents | 
**body** | **str** | The body of the schema | [optional] 

## Example

```python
from lusid.models.dialect_schema import DialectSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DialectSchema from a JSON string
dialect_schema_instance = DialectSchema.from_json(json)
# print the JSON string representation of the object
print DialectSchema.to_json()

# convert the object into a dict
dialect_schema_dict = dialect_schema_instance.to_dict()
# create an instance of DialectSchema from a dict
dialect_schema_form_dict = dialect_schema.from_dict(dialect_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


