# DialectId

Unique identifier of a given Dialect

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | The Scope of the dialect. | 
**vendor** | **str** | The vendor of the dialect, the entity that created it. e.g. ISDA, FINBOURNE. | 
**source_system** | **str** | The source system of the dialect, the system that understands it. e.g. LUSID, QuantLib. | 
**version** | **str** | The semantic version of the dialect: MAJOR.MINOR.PATCH. | 
**serialisation_format** | **str** | The serialisation format of a document in this dialect. e.g. JSON, XML. | 
**entity_type** | **str** | The type of entity this dialect describes e.g. Instrument. | 

## Example

```python
from lusid.models.dialect_id import DialectId

# TODO update the JSON string below
json = "{}"
# create an instance of DialectId from a JSON string
dialect_id_instance = DialectId.from_json(json)
# print the JSON string representation of the object
print DialectId.to_json()

# convert the object into a dict
dialect_id_dict = dialect_id_instance.to_dict()
# create an instance of DialectId from a dict
dialect_id_form_dict = dialect_id.from_dict(dialect_id_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


