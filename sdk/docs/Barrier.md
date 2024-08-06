# Barrier

Barrier class for exotic FxOption

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | **str** | Supported string (enumeration) values are: [Down, Up]. | 
**level** | **float** | Trigger level, which the underlying should (or should not) cross/touch. | 
**monitoring** | **str** | Supported string (enumeration) values are: [European, Bermudan, American]. | [optional] 
**type** | **str** | Supported string (enumeration) values are: [Knockin, Knockout]. | 

## Example

```python
from lusid.models.barrier import Barrier

# TODO update the JSON string below
json = "{}"
# create an instance of Barrier from a JSON string
barrier_instance = Barrier.from_json(json)
# print the JSON string representation of the object
print Barrier.to_json()

# convert the object into a dict
barrier_dict = barrier_instance.to_dict()
# create an instance of Barrier from a dict
barrier_form_dict = barrier.from_dict(barrier_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


