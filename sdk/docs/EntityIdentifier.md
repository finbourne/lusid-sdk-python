# EntityIdentifier

Dto to expose mapped keys to new standardised format

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier_scope** | **str** | The scope of the identifier | [optional] 
**identifier_type** | **str** | The type of the identifier | 
**identifier_value** | **str** | The value of the identifier | 

## Example

```python
from lusid.models.entity_identifier import EntityIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of EntityIdentifier from a JSON string
entity_identifier_instance = EntityIdentifier.from_json(json)
# print the JSON string representation of the object
print EntityIdentifier.to_json()

# convert the object into a dict
entity_identifier_dict = entity_identifier_instance.to_dict()
# create an instance of EntityIdentifier from a dict
entity_identifier_form_dict = entity_identifier.from_dict(entity_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


