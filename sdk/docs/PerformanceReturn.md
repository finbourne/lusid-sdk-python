# PerformanceReturn

A list of Returns.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_at** | **datetime** | The effectiveAt for the return. | 
**rate_of_return** | **float** | The return number. | 
**opening_market_value** | **float** | The opening market value. | [optional] 
**closing_market_value** | **float** | The closing market value. | [optional] 
**period** | **str** | Upsert the returns on a Daily or Monthly period. Defaults to Daily. | [optional] 

## Example

```python
from lusid.models.performance_return import PerformanceReturn

# TODO update the JSON string below
json = "{}"
# create an instance of PerformanceReturn from a JSON string
performance_return_instance = PerformanceReturn.from_json(json)
# print the JSON string representation of the object
print PerformanceReturn.to_json()

# convert the object into a dict
performance_return_dict = performance_return_instance.to_dict()
# create an instance of PerformanceReturn from a dict
performance_return_form_dict = performance_return.from_dict(performance_return_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


