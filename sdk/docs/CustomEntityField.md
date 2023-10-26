# CustomEntityField


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the field in the custom entity type definition. | 
**value** | **object** | The value for the field. | [optional] 
**effective_from** | **datetime** | The effective datetime from which the field&#39;s value is valid. For timeVariant fields, this defaults to the beginning of time. | [optional] 
**effective_until** | **datetime** | The effective datetime until which the field&#39;s value is valid. If not supplied, the value will be valid indefinitely or until the next “effectiveFrom” date of the field. | [optional] 

## Example

```python
from lusid.models.custom_entity_field import CustomEntityField

# TODO update the JSON string below
json = "{}"
# create an instance of CustomEntityField from a JSON string
custom_entity_field_instance = CustomEntityField.from_json(json)
# print the JSON string representation of the object
print CustomEntityField.to_json()

# convert the object into a dict
custom_entity_field_dict = custom_entity_field_instance.to_dict()
# create an instance of CustomEntityField from a dict
custom_entity_field_form_dict = custom_entity_field.from_dict(custom_entity_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


