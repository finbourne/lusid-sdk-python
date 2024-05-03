# StagedModificationDecision


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_at** | **datetime** | Time the decision request is made. | [optional] 
**user_id** | **str** | ID of user that approved the request. | [optional] 
**request_id** | **str** | ID of user that made the request. | [optional] 
**decision** | **str** | The decision on the requested staged modification, can be &#39;Approve&#39; or &#39;Reject&#39;. | [optional] 
**comment** | **str** | Comment on decision. | [optional] 

## Example

```python
from lusid.models.staged_modification_decision import StagedModificationDecision

# TODO update the JSON string below
json = "{}"
# create an instance of StagedModificationDecision from a JSON string
staged_modification_decision_instance = StagedModificationDecision.from_json(json)
# print the JSON string representation of the object
print StagedModificationDecision.to_json()

# convert the object into a dict
staged_modification_decision_dict = staged_modification_decision_instance.to_dict()
# create an instance of StagedModificationDecision from a dict
staged_modification_decision_form_dict = staged_modification_decision.from_dict(staged_modification_decision_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


