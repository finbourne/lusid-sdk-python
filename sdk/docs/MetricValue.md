# MetricValue


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** | The numerical value of the property. | [optional] 
**unit** | **str** |  | [optional] 

## Example

```python
from lusid.models.metric_value import MetricValue

# TODO update the JSON string below
json = "{}"
# create an instance of MetricValue from a JSON string
metric_value_instance = MetricValue.from_json(json)
# print the JSON string representation of the object
print MetricValue.to_json()

# convert the object into a dict
metric_value_dict = metric_value_instance.to_dict()
# create an instance of MetricValue from a dict
metric_value_form_dict = metric_value.from_dict(metric_value_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


