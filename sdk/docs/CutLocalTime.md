# CutLocalTime


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hours** | **int** |  | [optional] 
**minutes** | **int** |  | [optional] 

## Example

```python
from lusid.models.cut_local_time import CutLocalTime

# TODO update the JSON string below
json = "{}"
# create an instance of CutLocalTime from a JSON string
cut_local_time_instance = CutLocalTime.from_json(json)
# print the JSON string representation of the object
print CutLocalTime.to_json()

# convert the object into a dict
cut_local_time_dict = cut_local_time_instance.to_dict()
# create an instance of CutLocalTime from a dict
cut_local_time_form_dict = cut_local_time.from_dict(cut_local_time_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


