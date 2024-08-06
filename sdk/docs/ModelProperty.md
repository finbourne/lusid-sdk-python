# ModelProperty


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key of the property. This takes the format {domain}/{scope}/{code} e.g. &#39;Instrument/system/Name&#39; or &#39;Transaction/strategy/quantsignal&#39;. | 
**value** | [**PropertyValue**](PropertyValue.md) |  | [optional] 
**effective_from** | **datetime** | The effective datetime from which the property is valid. | [optional] 
**effective_until** | **datetime** | The effective datetime until which the property is valid. If not supplied this will be valid indefinitely, or until the next &#39;effectiveFrom&#39; datetime of the property. | [optional] 

## Example

```python
from lusid.models.model_property import ModelProperty

# TODO update the JSON string below
json = "{}"
# create an instance of ModelProperty from a JSON string
model_property_instance = ModelProperty.from_json(json)
# print the JSON string representation of the object
print ModelProperty.to_json()

# convert the object into a dict
model_property_dict = model_property_instance.to_dict()
# create an instance of ModelProperty from a dict
model_property_form_dict = model_property.from_dict(model_property_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


