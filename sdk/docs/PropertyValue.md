# PropertyValue

The value of the property.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label_value** | **str** | The text value of a property defined as having the &#39;Label&#39; type. | [optional] 
**metric_value** | [**MetricValue**](MetricValue.md) |  | [optional] 
**label_value_set** | [**LabelValueSet**](LabelValueSet.md) |  | [optional] 

## Example

```python
from lusid.models.property_value import PropertyValue

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyValue from a JSON string
property_value_instance = PropertyValue.from_json(json)
# print the JSON string representation of the object
print PropertyValue.to_json()

# convert the object into a dict
property_value_dict = property_value_instance.to_dict()
# create an instance of PropertyValue from a dict
property_value_form_dict = property_value.from_dict(property_value_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


