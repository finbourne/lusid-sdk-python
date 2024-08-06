# Touch

Touch class for exotic FxOption

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | **str** | Supported string (enumeration) values are: [Down, Up]. | 
**level** | **float** | Trigger level, which the underlying should (or should not) cross/touch. | 
**monitoring** | **str** | Supported string (enumeration) values are: [European, Bermudan, American]. | [optional] 
**type** | **str** | Supported string (enumeration) values are: [Touch, Notouch]. | 

## Example

```python
from lusid.models.touch import Touch

# TODO update the JSON string below
json = "{}"
# create an instance of Touch from a JSON string
touch_instance = Touch.from_json(json)
# print the JSON string representation of the object
print Touch.to_json()

# convert the object into a dict
touch_dict = touch_instance.to_dict()
# create an instance of Touch from a dict
touch_form_dict = touch.from_dict(touch_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


