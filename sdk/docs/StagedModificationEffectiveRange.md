# StagedModificationEffectiveRange


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_date** | **datetime** | The datetime that this requested change is effective from. | [optional] 
**until_date** | **datetime** | The datetime that this requested change is effective until. | [optional] 

## Example

```python
from lusid.models.staged_modification_effective_range import StagedModificationEffectiveRange

# TODO update the JSON string below
json = "{}"
# create an instance of StagedModificationEffectiveRange from a JSON string
staged_modification_effective_range_instance = StagedModificationEffectiveRange.from_json(json)
# print the JSON string representation of the object
print StagedModificationEffectiveRange.to_json()

# convert the object into a dict
staged_modification_effective_range_dict = staged_modification_effective_range_instance.to_dict()
# create an instance of StagedModificationEffectiveRange from a dict
staged_modification_effective_range_form_dict = staged_modification_effective_range.from_dict(staged_modification_effective_range_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


