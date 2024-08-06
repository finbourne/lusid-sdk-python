# Dialect

The language/format of a translatable entity. Entities can be LUSID native or external and the Dialect describes  1) the system that understands the entity and  2) applicable validation for the entity, in the form of a schema.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**DialectId**](DialectId.md) |  | 
**var_schema** | [**DialectSchema**](DialectSchema.md) |  | 
**version** | [**Version**](Version.md) |  | [optional] 

## Example

```python
from lusid.models.dialect import Dialect

# TODO update the JSON string below
json = "{}"
# create an instance of Dialect from a JSON string
dialect_instance = Dialect.from_json(json)
# print the JSON string representation of the object
print Dialect.to_json()

# convert the object into a dict
dialect_dict = dialect_instance.to_dict()
# create an instance of Dialect from a dict
dialect_form_dict = dialect.from_dict(dialect_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


