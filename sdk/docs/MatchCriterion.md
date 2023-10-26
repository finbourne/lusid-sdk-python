# MatchCriterion

A condition to be evaluated.  Each supported CriterionType has a corresponding schema.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**criterion_type** | **str** | The available values are: PropertyValueEquals, PropertyValueIn, SubHoldingKeyValueEquals | 

## Example

```python
from lusid.models.match_criterion import MatchCriterion

# TODO update the JSON string below
json = "{}"
# create an instance of MatchCriterion from a JSON string
match_criterion_instance = MatchCriterion.from_json(json)
# print the JSON string representation of the object
print MatchCriterion.to_json()

# convert the object into a dict
match_criterion_dict = match_criterion_instance.to_dict()
# create an instance of MatchCriterion from a dict
match_criterion_form_dict = match_criterion.from_dict(match_criterion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


