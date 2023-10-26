# LevelStep

Item which is stepped in level/quantity.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | The date from which the level should apply. | 
**quantity** | **float** | The quantity which is applied. This might be an absolute, percentage, fractional or other value. | 

## Example

```python
from lusid.models.level_step import LevelStep

# TODO update the JSON string below
json = "{}"
# create an instance of LevelStep from a JSON string
level_step_instance = LevelStep.from_json(json)
# print the JSON string representation of the object
print LevelStep.to_json()

# convert the object into a dict
level_step_dict = level_step_instance.to_dict()
# create an instance of LevelStep from a dict
level_step_form_dict = level_step.from_dict(level_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


