# StagedModificationDecisionRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**decision** | **str** | The decision on the requested staged modification, can be &#39;Approve&#39; or &#39;Reject&#39;. | 
**comment** | **str** | Comment on decision. | 

## Example

```python
from lusid.models.staged_modification_decision_request import StagedModificationDecisionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StagedModificationDecisionRequest from a JSON string
staged_modification_decision_request_instance = StagedModificationDecisionRequest.from_json(json)
# print the JSON string representation of the object
print StagedModificationDecisionRequest.to_json()

# convert the object into a dict
staged_modification_decision_request_dict = staged_modification_decision_request_instance.to_dict()
# create an instance of StagedModificationDecisionRequest from a dict
staged_modification_decision_request_form_dict = staged_modification_decision_request.from_dict(staged_modification_decision_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


