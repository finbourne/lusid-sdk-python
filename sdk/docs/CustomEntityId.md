# CustomEntityId


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier_scope** | **str** | The scope the identifier resides in (the scope of the identifier property definition). | 
**identifier_type** | **str** | What the identifier represents (the code of the identifier property definition). | 
**identifier_value** | **str** | The value of the identifier for this entity. | 
**effective_from** | **datetime** | The effective datetime from which the identifier is valid. | [optional] 
**effective_until** | **datetime** | The effective datetime until which the identifier is valid. If not supplied this will be valid indefinitely, or until the next &#39;effectiveFrom&#39; datetime of the identifier. | [optional] 

## Example

```python
from lusid.models.custom_entity_id import CustomEntityId

# TODO update the JSON string below
json = "{}"
# create an instance of CustomEntityId from a JSON string
custom_entity_id_instance = CustomEntityId.from_json(json)
# print the JSON string representation of the object
print CustomEntityId.to_json()

# convert the object into a dict
custom_entity_id_dict = custom_entity_id_instance.to_dict()
# create an instance of CustomEntityId from a dict
custom_entity_id_form_dict = custom_entity_id.from_dict(custom_entity_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


