# PerpetualProperty


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key of the property. This takes the format {domain}/{scope}/{code} e.g. &#39;Instrument/system/Name&#39; or &#39;Transaction/strategy/quantsignal&#39;. | 
**value** | [**PropertyValue**](PropertyValue.md) |  | [optional] 

## Example

```python
from lusid.models.perpetual_property import PerpetualProperty

# TODO update the JSON string below
json = "{}"
# create an instance of PerpetualProperty from a JSON string
perpetual_property_instance = PerpetualProperty.from_json(json)
# print the JSON string representation of the object
print PerpetualProperty.to_json()

# convert the object into a dict
perpetual_property_dict = perpetual_property_instance.to_dict()
# create an instance of PerpetualProperty from a dict
perpetual_property_form_dict = perpetual_property.from_dict(perpetual_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


