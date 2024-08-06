# PropertyInterval


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**PropertyValue**](PropertyValue.md) |  | 
**effective_range** | [**DateRange**](DateRange.md) |  | 
**as_at_range** | [**DateRange**](DateRange.md) |  | 
**status** | **str** | Indicates whether the value is part of the prevailing effective date timeline for the requested asAt date, or whether it has been superseded by correctional activity | 

## Example

```python
from lusid.models.property_interval import PropertyInterval

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyInterval from a JSON string
property_interval_instance = PropertyInterval.from_json(json)
# print the JSON string representation of the object
print PropertyInterval.to_json()

# convert the object into a dict
property_interval_dict = property_interval_instance.to_dict()
# create an instance of PropertyInterval from a dict
property_interval_form_dict = property_interval.from_dict(property_interval_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


